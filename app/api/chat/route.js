import { NextResponse } from "next/server"

// ---- Conversation Detection ----
function esSaludo(texto) {
  const saludos = [
    "hola", "buenas", "buenos días", "buenos dias", "buenas tardes",
    "buenas noches", "hey", "qué tal", "que tal", "saludos", "holi",
  ]
  const lower = texto.toLowerCase().trim()
  return saludos.some((s) => lower.includes(s))
}

function esDespedida(texto) {
  const despedidas = [
    "adiós", "adios", "hasta luego", "chao", "bye", "nos vemos",
    "hasta pronto", "me voy", "chau",
  ]
  const lower = texto.toLowerCase().trim()
  return despedidas.some((d) => lower.includes(d))
}

function esAgradecimiento(texto) {
  const agradecimientos = [
    "gracias", "thanks", "thank you", "muchas gracias",
    "te lo agradezco", "genial", "perfecto", "excelente",
  ]
  const lower = texto.toLowerCase().trim()
  return agradecimientos.some((a) => lower.includes(a))
}

function responderConversacion(comando) {
  if (esSaludo(comando)) {
    const hora = new Date().getHours()
    if (hora < 12) return "Buenos dias! Soy tu asistente domotico. En que puedo ayudarte con tu hogar hoy?"
    if (hora < 20) return "Buenas tardes! Que necesitas que haga?"
    return "Buenas noches! Como puedo ayudarte?"
  }
  if (esDespedida(comando)) return "Hasta pronto! Que tengas un excelente dia."
  if (esAgradecimiento(comando)) return "De nada! Estoy aqui para ayudarte cuando lo necesites."
  const lower = comando.toLowerCase()
  if (["cómo estás", "como estas"].some((p) => lower.includes(p)))
    return "Estoy funcionando perfectamente! Listo para controlar tu hogar. Que necesitas?"
  if (["ayuda", "help", "comandos"].some((p) => lower.includes(p)))
    return `Puedo ayudarte con:\n- Encender/apagar: luces, ventiladores, TV, electrodomesticos\n- Temperatura: ajustar calefaccion o aire acondicionado\n- Musica: reproducir canciones y artistas\n\nEjemplos:\n  "enciende la luz del comedor"\n  "apaga el ventilador del dormitorio"\n  "pon la calefaccion a 22 grados"\n  "reproduce Never Gonna Give You Up de Rick Astley"`
  return null
}

// ---- Device / Location Extraction ----
function extraerDispositivo(cmd) {
  const map = {
    luz: ["luz", "luces", "lámpara", "lampara"],
    ventilador: ["ventilador"],
    televisor: ["televisor", "tv", "tele"],
    horno: ["horno"],
    cafetera: ["cafetera"],
  }
  for (const [device, keywords] of Object.entries(map)) {
    if (keywords.some((k) => cmd.includes(k))) return device
  }
  return "dispositivo"
}

function extraerUbicacion(cmd) {
  const map = {
    comedor: ["comedor", "salon", "salón"],
    dormitorio: ["dormitorio", "habitación", "habitacion", "cuarto"],
    cocina: ["cocina"],
    "baño": ["baño", "bano"],
  }
  for (const [loc, keywords] of Object.entries(map)) {
    if (keywords.some((k) => cmd.includes(k))) return loc
  }
  return "sala principal"
}

// ---- Command Parser (fallback logic from parser.py) ----
function interpretarComando(comando) {
  const cmd = comando.toLowerCase().trim()

  if (["enciende", "encienda", "activar", "activa", "prende"].some((p) => cmd.includes(p))) {
    return {
      accion: "encender",
      dispositivo: extraerDispositivo(cmd),
      ubicacion: extraerUbicacion(cmd),
    }
  }

  if (["apaga", "apague", "desactiva", "desconecta"].some((p) => cmd.includes(p))) {
    return {
      accion: "apagar",
      dispositivo: extraerDispositivo(cmd),
      ubicacion: extraerUbicacion(cmd),
    }
  }

  if (cmd.includes("grados") || cmd.includes("temperatura")) {
    let modo = null
    if (cmd.includes("calefacción") || cmd.includes("calefaccion")) modo = "calefaccion"
    else if (cmd.includes("aire")) modo = "aire acondicionado"
    const match = cmd.match(/(\d+)\s*grados?/)
    const temp = match ? parseInt(match[1], 10) : null
    return { accion: "temperatura", temperatura: temp, modo: modo || "climatizacion" }
  }

  if (["pon", "reproduce", "play", "música", "musica"].some((p) => cmd.includes(p))) {
    const match = cmd.match(/(?:pon|reproduce|reproducir|poner)\s+(.+?)\s+de\s+(.+)/)
    if (match) {
      return { accion: "musica", cancion: match[1].trim(), artista: match[2].trim() }
    }
    return { accion: "musica", cancion: "seleccion aleatoria", artista: "varios artistas" }
  }

  return null
}

// ---- Action Executor (logic from acciones.py) ----
function ejecutarAccion(accion) {
  if (!accion) return "No se pudo interpretar el comando."
  switch (accion.accion) {
    case "encender":
      return `Encendiendo ${accion.dispositivo} en ${accion.ubicacion}.`
    case "apagar":
      return `Apagando ${accion.dispositivo} en ${accion.ubicacion}.`
    case "temperatura":
      return `Ajustando ${accion.modo} a ${accion.temperatura || 20} grados C.`
    case "musica":
      return `Reproduciendo '${accion.cancion}' de ${accion.artista}.`
    default:
      return "Accion no reconocida."
  }
}

// ---- API Handler ----
export async function POST(request) {
  try {
    const body = await request.json()
    const comando = (body.command || "").trim()

    if (!comando) {
      return NextResponse.json(
        { error: "Command cannot be empty" },
        { status: 400 }
      )
    }

    // 1. Check conversation
    const conversationResponse = responderConversacion(comando)
    if (conversationResponse) {
      return NextResponse.json({
        response: conversationResponse,
        action_type: "conversation",
      })
    }

    // 2. Parse smart-home command
    const accionParseada = interpretarComando(comando)
    if (accionParseada) {
      const resultado = ejecutarAccion(accionParseada)
      return NextResponse.json({
        response: resultado,
        action_type: "command",
        details: accionParseada,
      })
    }

    // 3. Unknown
    return NextResponse.json({
      response: "No entendi ese comando. Intenta ser mas especifico o escribe 'ayuda'.",
      action_type: "unknown",
    })
  } catch (error) {
    console.error("Error processing command:", error)
    return NextResponse.json(
      { response: "Ocurrio un error interno.", action_type: "error" },
      { status: 500 }
    )
  }
}
