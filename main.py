"""
Asistente Domótico Simulado
Archivo principal que gestiona la interfaz de usuario y coordina el sistema
"""

import os
from parser import interpretar_comando
from acciones import ejecutar_accion

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del sistema"""
    limpiar_pantalla()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "🏠 ASISTENTE DOMÓTICO INTELIGENTE 🤖" + " " * 11 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    print("💬 Puedes hablarme de forma natural. Ejemplos:")
    print("   • enciende la luz del comedor")
    print("   • pon la calefacción a 22 grados")
    print("   • reproduce música de Rick Astley")
    print()
    print("📝 Escribe 'salir' para terminar | 'limpiar' para limpiar pantalla")
    print("─" * 60)
    print()

def es_saludo(texto):
    """Detecta si el mensaje es un saludo"""
    saludos = ['hola', 'buenas', 'buenos días', 'buenos dias', 'buenas tardes', 
               'buenas noches', 'hey', 'qué tal', 'que tal', 'saludos', 'holi']
    texto_lower = texto.lower().strip()
    return any(saludo in texto_lower for saludo in saludos)

def es_despedida(texto):
    """Detecta si el mensaje es una despedida"""
    despedidas = ['adiós', 'adios', 'hasta luego', 'chao', 'bye', 'nos vemos', 
                  'hasta pronto', 'me voy', 'chau']
    texto_lower = texto.lower().strip()
    return any(despedida in texto_lower for despedida in despedidas)

def es_agradecimiento(texto):
    """Detecta si el mensaje es un agradecimiento"""
    agradecimientos = ['gracias', 'thanks', 'thank you', 'muchas gracias', 
                       'te lo agradezco', 'genial', 'perfecto', 'excelente']
    texto_lower = texto.lower().strip()
    return any(agradecimiento in texto_lower for agradecimiento in agradecimientos)

def responder_conversacion(comando):
    """Responde a mensajes conversacionales (saludos, despedidas, etc.)"""
    
    if es_saludo(comando):
        import datetime
        hora = datetime.datetime.now().hour
        if hora < 12:
            return "¡Buenos días! 🌅 ¿En qué puedo ayudarte con tu hogar hoy?"
        elif hora < 20:
            return "¡Buenas tardes! ☀️ ¿Qué necesitas que haga?"
        else:
            return "¡Buenas noches! 🌙 ¿Cómo puedo ayudarte?"
    
    elif es_despedida(comando):
        return "¡Hasta pronto! 👋 Que tengas un excelente día."
    
    elif es_agradecimiento(comando):
        return "¡De nada! 😊 Estoy aquí para ayudarte cuando lo necesites."
    
    elif any(palabra in comando.lower() for palabra in ['cómo estás', 'como estas', 'qué tal', 'que tal']):
        return "¡Estoy funcionando perfectamente! ⚡ Listo para controlar tu hogar. ¿Qué necesitas?"
    
    elif any(palabra in comando.lower() for palabra in ['ayuda', 'help', 'comandos']):
        return """
📋 Puedo ayudarte con:
   🔆 Encender/apagar: luces, ventiladores, TV, electrodomésticos
   🌡️  Temperatura: ajustar calefacción o aire acondicionado
   🎵 Música: reproducir canciones y artistas
   
Ejemplos:
   • "enciende la luz del comedor"
   • "apaga el ventilador del dormitorio"
   • "pon la calefacción a 22 grados"
   • "reproduce Never Gonna Give You Up de Rick Astley"
"""
    
    return None

def main():
    """Función principal del asistente domótico"""
    mostrar_bienvenida()
    
    while True:
        try:
            # Solicitar comando al usuario
            comando = input("💬 Tú > ").strip()
            
            # Verificar si el usuario quiere salir
            if comando.lower() in ['salir', 'exit', 'quit']:
                print("\n👋 Cerrando asistente domótico. ¡Hasta pronto!\n")
                break
            
            # Verificar si el usuario quiere limpiar la pantalla
            if comando.lower() in ['limpiar', 'clear', 'cls']:
                mostrar_bienvenida()
                continue
            
            # Ignorar entradas vacías
            if not comando:
                continue
            
            # Primero verificar si es una conversación
            respuesta_conversacion = responder_conversacion(comando)
            if respuesta_conversacion:
                print(f"🤖 Asistente > {respuesta_conversacion}\n")
                continue
            
            # Si no es conversación, interpretar como comando domótico
            accion_parseada = interpretar_comando(comando)
            
            # Ejecutar la acción interpretada
            if accion_parseada:
                resultado = ejecutar_accion(accion_parseada)
                print(f"🤖 Asistente > {resultado}\n")
            else:
                print("🤖 Asistente > No entendí ese comando. Escribe 'ayuda' para ver ejemplos.\n")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido. ¡Hasta pronto!\n")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}\n")

if __name__ == "__main__":
    main()