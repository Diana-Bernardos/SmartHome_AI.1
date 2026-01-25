"""
Parser de comandos usando LLM local (Ollama)
Interpreta órdenes en lenguaje natural usando inteligencia artificial REAL
"""

import requests
import json
import re

# Configuración de Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi3"  # Cambia a "llama3.2" o "mistral" si los descargaste
DEBUG_MODE = False  # Cambia a True para ver mensajes técnicos del LLM

def interpretar_comando_con_llm(comando):
    """
    Usa un LLM local (Ollama) para interpretar el comando
    
    Args:
        comando (str): Texto del comando ingresado por el usuario
    
    Returns:
        dict: Diccionario con la acción y sus parámetros, o None si falla
    """
    
    # Prompt para el LLM - VERSIÓN OPTIMIZADA
    prompt = f"""Convierte este comando en JSON:

COMANDO: "{comando}"

ACCIONES VÁLIDAS:
- encender: luz/ventilador/horno/tv
- apagar: luz/ventilador/horno/tv
- temperatura: calefacción/aire acondicionado + grados
- musica: canción + artista
- desconocida: si NO es comando domótico

FORMATO (usa "dispositivo" NO "dispositvo"):
{{"accion":"...","dispositivo":"...","ubicacion":"...","temperatura":null,"modo":null,"cancion":null,"artista":null}}

EJEMPLOS:
"enciende la luz del comedor" → {{"accion":"encender","dispositivo":"luz","ubicacion":"comedor","temperatura":null,"modo":null,"cancion":null,"artista":null}}
"pon calefacción a 22" → {{"accion":"temperatura","dispositivo":null,"ubicacion":null,"temperatura":22,"modo":"calefacción","cancion":null,"artista":null}}
"hola" → {{"accion":"desconocida","dispositivo":null,"ubicacion":null,"temperatura":null,"modo":null,"cancion":null,"artista":null}}

JSON:"""

    try:
        # Llamar a Ollama
        payload = {
            "model": MODELO,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.0,  # Más determinista = más rápido
            "options": {
                "num_predict": 150,  # Reducido para respuestas más rápidas
                "top_k": 10,
                "top_p": 0.5
            }
        }
        
        if DEBUG_MODE:
            print("🤖 Consultando LLM local...")
        
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        
        if response.status_code != 200:
            return interpretar_comando_fallback(comando)
        
        # Extraer respuesta
        resultado = response.json()
        texto_llm = resultado.get('response', '').strip()
        
        # Limpiar y extraer JSON
        json_parseado = extraer_json(texto_llm)
        
        if json_parseado:
            return json_parseado
        else:
            return interpretar_comando_fallback(comando)
            
    except requests.exceptions.ConnectionError:
        # Silencioso - solo usa fallback
        return interpretar_comando_fallback(comando)
    except requests.exceptions.Timeout:
        # Silencioso - solo usa fallback
        return interpretar_comando_fallback(comando)
    except Exception as e:
        # Silencioso - solo usa fallback
        return interpretar_comando_fallback(comando)

def extraer_json(texto):
    """
    Extrae y parsea JSON de la respuesta del LLM
    """
    try:
        # Limpiar markdown si existe
        texto = re.sub(r'```json\s*', '', texto)
        texto = re.sub(r'```\s*', '', texto)
        texto = texto.strip()
        
        # Intentar encontrar el JSON en el texto
        match = re.search(r'\{.*\}', texto, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        
        # Si no hay {}, intentar parsear directamente
        return json.loads(texto)
        
    except json.JSONDecodeError:
        return None

def interpretar_comando_fallback(comando):
    """
    Sistema de respaldo si el LLM falla (versión simple con reglas)
    """
    comando = comando.lower().strip()
    
    # Detectar acción de ENCENDER
    if any(palabra in comando for palabra in ['enciende', 'encienda', 'activar', 'activa', 'prende']):
        return {
            'accion': 'encender',
            'dispositivo': extraer_dispositivo(comando),
            'ubicacion': extraer_ubicacion(comando),
            'temperatura': None,
            'modo': None,
            'cancion': None,
            'artista': None
        }
    
    # Detectar acción de APAGAR
    elif any(palabra in comando for palabra in ['apaga', 'apague', 'desactiva', 'desconecta']):
        return {
            'accion': 'apagar',
            'dispositivo': extraer_dispositivo(comando),
            'ubicacion': extraer_ubicacion(comando),
            'temperatura': None,
            'modo': None,
            'cancion': None,
            'artista': None
        }
    
    # Detectar TEMPERATURA
    elif 'grados' in comando or 'temperatura' in comando:
        modo = None
        if 'calefacción' in comando or 'calefaccion' in comando:
            modo = 'calefacción'
        elif 'aire' in comando:
            modo = 'aire acondicionado'
        
        match = re.search(r'(\d+)\s*grados?', comando)
        temp = int(match.group(1)) if match else None
        
        return {
            'accion': 'temperatura',
            'dispositivo': None,
            'ubicacion': None,
            'temperatura': temp,
            'modo': modo,
            'cancion': None,
            'artista': None
        }
    
    # Detectar MÚSICA
    elif any(palabra in comando for palabra in ['pon', 'reproduce', 'play']):
        match = re.search(r'(?:pon|reproduce|reproducir|poner)\s+(.+?)\s+de\s+(.+)', comando)
        if match:
            return {
                'accion': 'musica',
                'dispositivo': None,
                'ubicacion': None,
                'temperatura': None,
                'modo': None,
                'cancion': match.group(1).strip(),
                'artista': match.group(2).strip()
            }
    
    return None

def extraer_dispositivo(comando):
    """Identifica el dispositivo mencionado"""
    dispositivos = {
        'luz': ['luz', 'luces', 'lámpara'],
        'ventilador': ['ventilador'],
        'televisor': ['televisor', 'tv', 'tele'],
        'horno': ['horno'],
        'cafetera': ['cafetera'],
    }
    
    for dispositivo, palabras in dispositivos.items():
        if any(palabra in comando for palabra in palabras):
            return dispositivo
    return 'dispositivo'

def extraer_ubicacion(comando):
    """Identifica la ubicación mencionada"""
    ubicaciones = {
        'comedor': ['comedor', 'salon'],
        'dormitorio': ['dormitorio', 'habitación', 'cuarto'],
        'cocina': ['cocina'],
        'baño': ['baño', 'bano'],
    }
    
    for ubicacion, palabras in ubicaciones.items():
        if any(palabra in comando for palabra in palabras):
            return ubicacion
    return 'sala principal'

# Función principal que se usa desde main.py
def interpretar_comando(comando):
    """
    Función principal de interpretación (usa LLM + fallback)
    """
    return interpretar_comando_con_llm(comando)