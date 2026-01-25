# 🏠 Asistente Domótico Inteligente con IA - Sistema Conversacional

## 📋 Descripción del Proyecto

Este proyecto implementa un **asistente domótico inteligente y conversacional** capaz de interpretar comandos en lenguaje natural para controlar dispositivos del hogar. El sistema utiliza un **LLM (Large Language Model) REAL y GRATUITO** mediante **Ollama** para analizar las órdenes del usuario y ejecutar las acciones correspondientes.

**Novedad**: El asistente ahora puede **conversar contigo** de forma natural, respondiendo a saludos, despedidas, agradecimientos y preguntas casuales, además de controlar tu hogar inteligente.

A diferencia de sistemas tradicionales con reglas fijas, este proyecto usa **Inteligencia Artificial real** para comprender el lenguaje humano de forma natural y flexible, permitiendo comandos variados y conversacionales.

### ¿Qué es un LLM?

Un **LLM (Large Language Model)** es un modelo de inteligencia artificial entrenado con enormes cantidades de texto para comprender y generar lenguaje humano. Estos modelos utilizan arquitecturas de redes neuronales profundas, típicamente basadas en transformers, que procesan texto analizando las relaciones contextuales entre palabras.

#### Características principales de un LLM:

- **Procesamiento del lenguaje natural (NLP)**: Comprenden la sintaxis, semántica y contexto del lenguaje humano
- **Aprendizaje profundo**: Se entrenan con millones o miles de millones de parámetros
- **Versatilidad**: Pueden realizar múltiples tareas: traducción, resumen, clasificación, generación de código, etc.
- **Comprensión contextual**: Entienden instrucciones ambiguas y extraen la intención del usuario

Ejemplos de LLMs populares incluyen GPT (OpenAI), Claude (Anthropic), LLaMA (Meta) o Phi (Microsoft).

### ¿Por qué usar Ollama?

**Ollama** es una plataforma que permite ejecutar LLMs potentes **localmente en tu ordenador**, sin necesidad de conexión a internet ni costes de API. Esto ofrece:

- ✅ **100% Gratuito** - Sin límites de uso ni pagos mensuales
- ✅ **Privacidad total** - Tus comandos no salen de tu ordenador
- ✅ **Funciona offline** - No necesita conexión a internet
- ✅ **Sin límites** - Usa el asistente cuanto quieras
- ✅ **Modelos potentes** - Acceso a Phi, LLaMA, Mistral y más

---

## 🎯 Funcionalidades

### 💬 **Conversación Natural** (¡NUEVO!)

El asistente ahora puede mantener conversaciones naturales:

#### **Saludos contextuales**
```
💬 Tú > hola
🤖 Asistente > ¡Buenos días! 🌅 ¿En qué puedo ayudarte con tu hogar hoy?

💬 Tú > buenas noches
🤖 Asistente > ¡Buenas noches! 🌙 ¿Cómo puedo ayudarte?
```

El asistente responde diferente según la hora del día:
- 🌅 **Antes de 12h**: "¡Buenos días!"
- ☀️ **12h-20h**: "¡Buenas tardes!"
- 🌙 **Después de 20h**: "¡Buenas noches!"

#### **Despedidas**
```
💬 Tú > adiós
🤖 Asistente > ¡Hasta pronto! 👋 Que tengas un excelente día.

💬 Tú > hasta luego
🤖 Asistente > ¡Hasta pronto! 👋 Que tengas un excelente día.
```

#### **Agradecimientos**
```
💬 Tú > gracias
🤖 Asistente > ¡De nada! 😊 Estoy aquí para ayudarte cuando lo necesites.

💬 Tú > perfecto
🤖 Asistente > ¡De nada! 😊 Estoy aquí para ayudarte cuando lo necesites.
```

#### **Preguntas casuales**
```
💬 Tú > ¿cómo estás?
🤖 Asistente > ¡Estoy funcionando perfectamente! ⚡ Listo para controlar tu hogar. ¿Qué necesitas?

💬 Tú > ¿qué tal?
🤖 Asistente > ¡Estoy funcionando perfectamente! ⚡ Listo para controlar tu hogar. ¿Qué necesitas?
```

#### **Sistema de ayuda integrado**
```
💬 Tú > ayuda
🤖 Asistente > 
📋 Puedo ayudarte con:
   🔆 Encender/apagar: luces, ventiladores, TV, electrodomésticos
   🌡️  Temperatura: ajustar calefacción o aire acondicionado
   🎵 Música: reproducir canciones y artistas
   
Ejemplos:
   • "enciende la luz del comedor"
   • "apaga el ventilador del dormitorio"
   • "pon la calefacción a 22 grados"
   • "reproduce Never Gonna Give You Up de Rick Astley"
```

---

### 🏠 **Control Domótico con IA**

El asistente reconoce y ejecuta cuatro tipos de acciones mediante IA:

#### **1. Encender dispositivos**
```
✅ "enciende la luz del comedor"
✅ "activa el ventilador del dormitorio"
✅ "prende la tele de la sala"
✅ "enciende el horno"
```

#### **2. Apagar dispositivos**
```
✅ "apaga la luz del comedor"
✅ "desconecta el horno"
✅ "desactiva el aire acondicionado"
✅ "apaga el ventilador del dormitorio"
```

#### **3. Ajustar temperatura**
```
✅ "pon la calefacción a 22 grados"
✅ "enciende el aire a 18 grados"
✅ "hace calor, baja la temperatura a 20"
✅ "ajusta la calefacción a 24°C"
```

#### **4. Reproducir música**
```
✅ "reproduce Never Gonna Give You Up de Rick Astley"
✅ "pon música de Queen"
✅ "ponme algo de Coldplay"
✅ "reproduce mi canción favorita"
```

---

### 🎨 **Interface Mejorada** (¡NUEVO!)

La terminal ahora tiene un diseño limpio y profesional:

```
╔═════════════════════════════════════════════════════════╗
║          🏠 ASISTENTE DOMÓTICO INTELIGENTE 🤖           ║
╚═════════════════════════════════════════════════════════╝

💬 Puedes hablarme de forma natural. Ejemplos:
   • enciende la luz del comedor
   • pon la calefacción a 22 grados
   • reproduce música de Rick Astley

📝 Escribe 'salir' para terminar | 'limpiar' para limpiar pantalla
────────────────────────────────────────────────────────────

💬 Tú > 
```

#### **Características de la interfaz:**
- ✨ **Diseño limpio** con bordes decorativos
- 🎨 **Emojis contextuales** para mejor visualización
- 🧹 **Sin mensajes técnicos** (modo silencioso del LLM)
- 🔄 **Comando limpiar** para resetear la pantalla
- ⚡ **Respuestas rápidas** y concisas

---

### 🛠️ **Comandos Especiales del Sistema**

| Comando | Función | Ejemplo |
|---------|---------|---------|
| `limpiar` | Limpia la pantalla y muestra el menú inicial | `💬 Tú > limpiar` |
| `ayuda` | Muestra lista completa de comandos disponibles | `💬 Tú > ayuda` |
| `salir` | Cierra el asistente de forma elegante | `💬 Tú > salir` |
| `clear` | Alias de limpiar (también funciona `cls`) | `💬 Tú > clear` |

---

## 📁 Estructura del Proyecto

```
asistente_domotico/
│
├── main.py              # Interfaz conversacional y control de usuario
├── parser.py            # Motor de IA (Ollama) + sistema de respaldo
├── acciones.py          # Ejecución de acciones domóticas
├── pruebas.txt          # Registro de pruebas funcionales
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación completa
```

### Descripción detallada de archivos:

#### **main.py** - Control y conversación
- Gestiona la interfaz de usuario con diseño limpio
- Maneja saludos, despedidas y conversación natural
- Coordina entre parser y acciones
- Sistema de ayuda integrado
- Limpieza de pantalla automática

#### **parser.py** - Cerebro del sistema
- Usa **Ollama** (LLM local) para interpretar comandos
- Sistema de respaldo con reglas cuando LLM no disponible
- Modo DEBUG configurable
- Optimizado para velocidad y precisión

#### **acciones.py** - Ejecutor de acciones
- Implementa las 4 funciones principales
- Mensajes con emojis para mejor UX
- Manejo de valores por defecto
- Función `ejecutar_accion` que coordina todo

#### **requirements.txt** - Dependencias
```txt
requests
```

---

## 🚀 Instalación y Configuración

### Requisitos Previos

- **Python 3.7 o superior** instalado
- **Visual Studio Code** (recomendado)
- **4GB de RAM mínimo** para ejecutar el LLM
- **5GB de espacio en disco** para el modelo de IA

---

### Paso 1: Instalar Ollama

#### **Windows:**
1. Ve a: https://ollama.com/download
2. Descarga el instalador de Windows
3. Ejecuta el instalador (se inicia automáticamente)
4. Verifica abriendo CMD:
```bash
ollama --version
```

#### **Mac:**
```bash
# Descargar desde la web oficial: https://ollama.com/download
# O usar Homebrew:
brew install ollama
```

#### **Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

### Paso 2: Descargar un modelo de IA

Abre tu terminal y ejecuta:

```bash
# Opción 1: Modelo pequeño y rápido (RECOMENDADO)
ollama pull phi3

# Opción 2: Modelo tiny - ultra rápido para PCs lentos
ollama pull tinyllama

# Opción 3: Modelo balanceado (mejor precisión)
ollama pull llama3.2
```

**Recomendación**: 
- Si tu PC es **rápido** (8GB+ RAM): usa `phi3`
- Si tu PC es **lento** (4GB RAM): usa `tinyllama`

#### Verificar que se descargó:
```bash
ollama list
```

Deberías ver tu modelo en la lista.

---

### Paso 3: Instalar dependencias de Python

```bash
# Navega a la carpeta del proyecto
cd ruta/a/asistente_domotico

# Instala las dependencias
pip install -r requirements.txt

# O manualmente:
pip install requests
```

Si `pip` no funciona:
```bash
python -m pip install requests
```

---

### Paso 4: Configurar el modelo (opcional)

Abre `parser.py` y ajusta según tu modelo descargado:

```python
# Configuración de Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi3"  # Cambia a "tinyllama" o "llama3.2" si descargaste otro
DEBUG_MODE = False  # Cambia a True para ver mensajes técnicos del LLM
```

---

## ▶️ Cómo Ejecutar el Proyecto

### Método 1: Ejecución simple desde terminal

```bash
# Asegúrate de estar en la carpeta del proyecto
cd C:\Users\tu_usuario\Desktop\asistente_domotico

# Ejecuta el asistente
python main.py
```

### Método 2: Desde Visual Studio Code

1. **Abre VS Code**
2. **File** → **Open Folder** → Selecciona `asistente_domotico`
3. **Abre la terminal integrada**: `Ctrl + Ñ` o `View` → `Terminal`
4. **Ejecuta**:
```bash
python main.py
```

### Método 3: Con el botón Run de VS Code

1. Abre `main.py` en VS Code
2. Presiona `F5` o clic en "Run" → "Run Without Debugging"
3. La terminal integrada mostrará el asistente

### Método 4: Con el depurador (para desarrollo)

1. Ve a la vista de "Run and Debug" (`Ctrl+Shift+D`)
2. Clic en "Start Debugging" (F5)
3. Establece breakpoints para analizar el código

---

## 💬 Ejemplos de Uso Completos

### Sesión de ejemplo 1: Conversación y control básico

```
╔═════════════════════════════════════════════════════════╗
║          🏠 ASISTENTE DOMÓTICO INTELIGENTE 🤖           ║
╚═════════════════════════════════════════════════════════╝

💬 Tú > buenos días
🤖 Asistente > ¡Buenos días! 🌅 ¿En qué puedo ayudarte con tu hogar hoy?

💬 Tú > enciende la luz del comedor
🤖 Asistente > ✅ Encendiendo luz en comedor.

💬 Tú > hace frío
🤖 Asistente > 🌡️ Ajustando calefacción a 22°C.

💬 Tú > gracias
🤖 Asistente > ¡De nada! 😊 Estoy aquí para ayudarte cuando lo necesites.

💬 Tú > salir

👋 Cerrando asistente domótico. ¡Hasta pronto!
```

### Sesión de ejemplo 2: Control avanzado

```
💬 Tú > enciende el horno
🤖 Asistente > ✅ Encendiendo horno en cocina.

💬 Tú > pon la calefacción a 24 grados
🤖 Asistente > 🌡️ Ajustando calefacción a 24°C.

💬 Tú > reproduce música de Queen
🤖 Asistente > 🎵 Reproduciendo 'música' de Queen.

💬 Tú > apaga la luz del dormitorio
🤖 Asistente > ✅ Apagando luz en dormitorio.
```

### Sesión de ejemplo 3: Uso de ayuda

```
💬 Tú > ayuda
🤖 Asistente > 
📋 Puedo ayudarte con:
   🔆 Encender/apagar: luces, ventiladores, TV, electrodomésticos
   🌡️  Temperatura: ajustar calefacción o aire acondicionado
   🎵 Música: reproducir canciones y artistas
   
Ejemplos:
   • "enciende la luz del comedor"
   • "apaga el ventilador del dormitorio"
   • "pon la calefacción a 22 grados"
   • "reproduce Never Gonna Give You Up de Rick Astley"

💬 Tú > limpiar
[La pantalla se limpia y muestra el menú inicial de nuevo]
```

---

## 🎯 Lista Completa de Comandos Reconocidos

### Comandos Conversacionales

| Categoría | Comandos Reconocidos |
|-----------|---------------------|
| **Saludos** | hola, buenos días, buenas tardes, buenas noches, hey, qué tal, saludos |
| **Despedidas** | adiós, hasta luego, chao, bye, nos vemos, hasta pronto, me voy |
| **Agradecimientos** | gracias, muchas gracias, te lo agradezco, genial, perfecto, excelente |
| **Preguntas** | ¿cómo estás?, ¿qué tal?, ayuda, help, comandos |
| **Sistema** | limpiar, clear, cls, salir, exit, quit |

### Comandos Domóticos

| Acción | Verbos Reconocidos | Ejemplos |
|--------|-------------------|----------|
| **Encender** | enciende, encienda, activa, activar, prende, prenda | "enciende la luz", "activa el ventilador" |
| **Apagar** | apaga, apague, desactiva, desactivar, desconecta, desconectar | "apaga la luz", "desconecta el horno" |
| **Temperatura** | pon, ajusta, configura + temperatura/grados/calefacción/aire | "pon la calefacción a 22 grados" |
| **Música** | reproduce, pon, play, escuchar + canción/artista | "reproduce música de Queen" |

### Dispositivos Reconocidos

- 💡 **Luces**: luz, luces, lámpara, iluminación
- 🌀 **Ventilador**: ventilador, ventiladores
- 📺 **TV**: televisor, televisión, TV, tele
- 🔥 **Horno**: horno
- ☕ **Cafetera**: cafetera, café
- 🧺 **Lavadora**: lavadora
- 🌡️ **Calefacción**: calefacción, radiador
- ❄️ **Aire**: aire acondicionado, aire, climatizador

### Ubicaciones Reconocidas

- 🍽️ **Comedor**: comedor, salón, sala
- 🛏️ **Dormitorio**: dormitorio, habitación, cuarto, recámara
- 🍳 **Cocina**: cocina
- 🚿 **Baño**: baño, aseo
- 🚪 **Pasillo**: pasillo
- 🏡 **Entrada**: entrada, recibidor
- 🚗 **Garaje**: garaje
- 🌳 **Jardín**: jardín, exterior

---

## 🔧 Uso del Depurador en VS Code

### Configurar el Depurador

1. **Crear configuración de depuración**:
   - Presiona `Ctrl+Shift+D` para abrir Run and Debug
   - Clic en "create a launch.json file"
   - Seleccionar "Python File"

2. **Establecer breakpoints**:
   - Abre `main.py`, `parser.py` o `acciones.py`
   - Clic en el margen izquierdo junto al número de línea (aparece un punto rojo)

3. **Iniciar depuración**:
   - Presiona `F5`
   - El programa se detendrá en los breakpoints

4. **Inspeccionar variables**:
   - Panel izquierdo muestra variables locales
   - Usa controles para avanzar línea a línea (F10, F11)

### Puntos de interrupción recomendados

```python
# main.py - Línea ~80
accion_parseada = interpretar_comando(comando)
# Ver el comando antes de procesarlo

# parser.py - Línea ~50
response = requests.post(OLLAMA_URL, json=payload, timeout=60)
# Ver la petición al LLM

# acciones.py - Línea ~67
tipo_accion = accion_parseada.get('accion')
# Ver el JSON parseado por el LLM
```

---

## 🚨 Solución de Problemas

### ❌ Error: "cannot import name 'ejecutar_accion'"

**Solución**: Asegúrate de que `acciones.py` contiene la función `ejecutar_accion` al final del archivo.

```python
# Al final de acciones.py debe estar:
def ejecutar_accion(accion_parseada):
    # ... código de la función
```

---

### ❌ Error: "No module named 'requests'"

**Solución**:
```bash
pip install requests
# O si no funciona:
python -m pip install requests
```

---

### ❌ Error: "Solo se permite un uso de cada dirección"

**Esto es NORMAL** - significa que Ollama ya está corriendo. Simplemente:

1. **No hagas** `ollama serve`
2. **Ejecuta** directamente `python main.py`

Ollama se inicia automáticamente en Windows.

---

### ⏱️ El LLM tarda mucho (>15 segundos)

**Soluciones**:

**Opción 1**: Usa un modelo más pequeño
```bash
ollama pull tinyllama
# En parser.py cambia: MODELO = "tinyllama"
```

**Opción 2**: Cierra otros programas para liberar RAM

**Opción 3**: Desactiva el LLM temporalmente
```python
# En parser.py cambia:
DEBUG_MODE = False  # Modo silencioso
# El sistema usará las reglas de respaldo (instantáneo)
```

---

### 🔍 Ver qué está haciendo el LLM (Modo Debug)

Si quieres ver los mensajes técnicos del LLM:

```python
# En parser.py cambia:
DEBUG_MODE = True
```

Verás mensajes como:
```
🤖 Consultando LLM local...
💭 Respuesta del LLM: {"accion":"encender"...}
✅ JSON parseado: {'accion': 'encender'...}
```

---

### 🧪 Verificar que Ollama funciona

```bash
# Ver modelos instalados
ollama list

# Probar el modelo directamente
ollama run phi3 "Hola, ¿cómo estás?"

# Debe responder algo coherente
```

---

## 🧪 Pruebas Realizadas

Se han ejecutado **15+ casos de prueba** documentados en `pruebas.txt`:

- ✅ 7 casos obligatorios del proyecto
- ✅ 5 casos adicionales de validación
- ✅ 3 casos de comandos naturales con LLM
- ✅ 5 casos de conversación natural (¡NUEVO!)
- ✅ 100% de tasa de éxito

Ver archivo `pruebas.txt` para detalles completos.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.7+
- **IDE**: Visual Studio Code
- **LLM**: Ollama (phi3, tinyllama, llama3.2 o mistral)
- **Librerías**: 
  - `requests` - Comunicación con Ollama
  - `re` - Expresiones regulares para parsing
  - `json` - Procesamiento de respuestas del LLM
  - `os` - Limpieza de pantalla multiplataforma
  - `datetime` - Saludos contextuales según hora
  - Librerías estándar de Python

---

## 🔄 Arquitectura del Sistema

### Flujo de ejecución completo:

```
Usuario ingresa texto
        ↓
main.py: ¿Es conversación? (saludo, despedida, etc.)
        ↓
    SI → Responde directamente
        ↓
    NO → parser.py: Envía al LLM (Ollama)
        ↓
LLM interpreta y devuelve JSON
        ↓
parser.py: Extrae la acción
        ↓
acciones.py: Ejecuta función correspondiente
        ↓
main.py: Muestra resultado al usuario
```

### Sistema de respaldo (fallback):

```
Parser detecta error/timeout del LLM
        ↓
Activa sistema de reglas con regex
        ↓
Usa palabras clave y patrones
        ↓
Devuelve acción (menos flexible pero funcional)
```

---

## 📚 Resultados de Aprendizaje

Este proyecto desarrolla las siguientes competencias:

### Módulo de Entornos de Desarrollo:
1. ✅ **Instalación y configuración** (VS Code + Python + Ollama + LLM)
2. ✅ **Uso de herramientas de edición** (breakpoints, inspección, terminal integrada)
3. ✅ **Organización de proyectos** (estructura modular, separación de responsabilidades)
4. ✅ **Pruebas funcionales** (casos documentados con resultados)
5. ✅ **Documentación técnica** (docstrings, comentarios, README completo)
6. ✅ **Control de versiones** (estructura compatible con Git)

### Aprendizajes adicionales sobre IA:
7. ✅ **Integración de LLMs** en aplicaciones reales
8. ✅ **Procesamiento de lenguaje natural** (NLP básico)
9. ✅ **Diseño de prompts** para IAs
10. ✅ **Manejo de APIs** (peticiones HTTP, JSON)
11. ✅ **Experiencia de usuario** (UX conversacional)
12. ✅ **Sistemas híbridos** (IA + reglas tradicionales)

---

## 🎓 ¿Qué Aprendiste con Este Proyecto?

### Sobre Inteligencia Artificial:
- Cómo funciona un LLM y cómo integrarlo
- Diferencia entre reglas deterministas y comprensión de IA
- Cómo diseñar prompts efectivos
- Manejo de respuestas impredecibles de IA

### Sobre Programación:
- Arquitectura modular (separación de responsabilidades)
- Manejo de errores y sistemas de respaldo
- Parsing de JSON y expresiones regulares
- Diseño de interfaces conversacionales

### Sobre Desarrollo:
- Uso profesional de VS Code
- Depuración con breakpoints
- Documentación de proyectos
- Testing y validación

---

## 🔮 Mejoras Futuras

### Corto plazo (fáciles):
1. ✅ **Historial de comandos** - Flecha arriba para repetir
2. ✅ **Más dispositivos** - Añadir soporte para frigorífico, lavavajillas, etc.
3. ✅ **Confirmaciones** - "¿Estás seguro de apagar todo?"
4. ✅ **Estados persistentes** - Recordar qué está encendido/apagado
5. ✅ **Colores en terminal** - Usar colorama para respuestas coloridas

### Medio plazo (intermedias):
6. **Base de datos** - SQLite para guardar estados e historial
7. **Interface gráfica** - GUI con Tkinter o PyQt
8. **Comandos múltiples** - "Enciende la luz y pon música"
9. **Rutinas programadas** - "Enciende calefacción a las 7 AM"
10. **Contexto conversacional** - "Apaga eso" después de "Enciende la luz"

### Largo plazo (avanzadas):
11. **IoT real** - Conectar con Philips Hue, Alexa, Google Home
12. **Voz** - Reconocimiento con `speech_recognition`
13. **Síntesis de voz** - Respuestas en audio con `pyttsx3`
14. **Aprendizaje continuo** - El sistema aprende de correcciones
15. **App móvil** - Control desde smartphone
16. **Multi-usuario** - Perfiles y preferencias personalizadas

---

## 📊 Comparación Final: Reglas vs LLM vs Conversacional

| Característica | Reglas Simples | LLM Solo | LLM + Conversación (Este proyecto) |
|----------------|---------------|----------|----------------------------------|
| **Costo** | ✅ Gratis | ✅ Gratis (local) | ✅ Gratis (local) |
| **Velocidad** | ⚡ Instantáneo | ⚡ 2-5 seg | ⚡ Instant/2-5 seg (híbrido) |
| **Flexibilidad** | ❌ Solo exactos | ✅ Natural | ✅✅ Muy natural |
| **Conversación** | ❌ No | ❌ Limitada | ✅✅ Completa |
| **UX** | ⭐⭐ Básica | ⭐⭐⭐ Buena | ⭐⭐⭐⭐⭐ Excelente |
| **Amigable** | ❌ Frío | ⭐⭐⭐ Funcional | ✅✅ Muy amigable |
| **Mantenimiento** | ❌ Alto | ✅ Bajo | ✅ Bajo |

---

## 👨‍💻 Autor

**[Tu Nombre]**  
Proyecto desarrollado para el módulo de Entornos de Desarrollo  
Fecha: Enero 2026

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## 📞 Soporte y Recursos

### Documentación de Ollama:
- **Web oficial**: https://ollama.com
- **Modelos disponibles**: https://ollama.com/library
- **GitHub**: https://github.com/ollama/ollama
- **Documentación API**: https://github.com/ollama/ollama/blob/main/docs/api.md

### Comandos útiles de Ollama:
```bash
ollama list              # Ver modelos instalados
ollama pull <modelo>     # Descargar un modelo
ollama rm <modelo>       # Eliminar un modelo
ollama run <modelo>      # Ejecutar en modo chat
ollama serve             # Iniciar servidor