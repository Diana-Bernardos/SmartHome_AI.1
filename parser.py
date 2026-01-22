"""
Parser de comandos para el asistente domótico
Interpreta las órdenes en lenguaje natural y las convierte en acciones estructuradas
"""

import re

def interpretar_comando(comando):
    """
    Analiza un comando en lenguaje natural y extrae la acción a realizar
    
    Args:
        comando (str): Texto del comando ingresado por el usuario
    
    Returns:
        dict: Diccionario con la acción y sus parámetros, o None si no se reconoce
    """
    comando = comando.lower().strip()
    
    # Detectar acción de ENCENDER
    if any(palabra in comando for palabra in ['enciende', 'encienda', 'activar', 'activa', 'prende', 'prenda']):
        return parsear_encender(comando)
    
    # Detectar acción de APAGAR
    elif any(palabra in comando for palabra in ['apaga', 'apague', 'desactiva', 'desactivar', 'desconecta', 'desconectar']):
        return parsear_apagar(comando)
    
    # Detectar acción de AJUSTAR TEMPERATURA
    elif any(palabra in comando for palabra in ['temperatura', 'grados', 'calefacción', 'calefaccion', 'aire acondicionado']):
        return parsear_temperatura(comando)
    
    # Detectar acción de REPRODUCIR MÚSICA
    elif any(palabra in comando for palabra in ['pon', 'reproduce', 'reproducir', 'poner', 'play', 'escuchar']):
        return parsear_musica(comando)
    
    return None

def parsear_encender(comando):
    """Extrae dispositivo y ubicación para comando de encendido"""
    dispositivo = extraer_dispositivo(comando)
    ubicacion = extraer_ubicacion(comando)
    
    if dispositivo and ubicacion:
        return {
            'accion': 'encender',
            'dispositivo': dispositivo,
            'ubicacion': ubicacion
        }
    return None

def parsear_apagar(comando):
    """Extrae dispositivo y ubicación para comando de apagado"""
    dispositivo = extraer_dispositivo(comando)
    ubicacion = extraer_ubicacion(comando)
    
    if dispositivo and ubicacion:
        return {
            'accion': 'apagar',
            'dispositivo': dispositivo,
            'ubicacion': ubicacion
        }
    return None

def parsear_temperatura(comando):
    """Extrae modo y temperatura para comando de climatización"""
    # Detectar modo (calefacción o aire acondicionado)
    modo = None
    if 'calefacción' in comando or 'calefaccion' in comando:
        modo = 'calefacción'
    elif 'aire acondicionado' in comando or 'aire' in comando:
        modo = 'aire acondicionado'
    
    # Extraer temperatura con expresión regular
    match = re.search(r'(\d+)\s*grados?', comando)
    temperatura = int(match.group(1)) if match else None
    
    if modo and temperatura:
        return {
            'accion': 'temperatura',
            'modo': modo,
            'temperatura': temperatura
        }
    return None

def parsear_musica(comando):
    """Extrae artista y canción para comando de reproducción musical"""
    # Intentar extraer canción y artista con patrón "canción de artista"
    match = re.search(r'(?:pon|reproduce|reproducir|poner)\s+(.+?)\s+de\s+(.+)', comando)
    
    if match:
        cancion = match.group(1).strip()
        artista = match.group(2).strip()
        return {
            'accion': 'musica',
            'cancion': cancion,
            'artista': artista
        }
    
    # Si no se encuentra el patrón, buscar solo después del verbo
    match_simple = re.search(r'(?:pon|reproduce|reproducir|poner)\s+(.+)', comando)
    if match_simple:
        contenido = match_simple.group(1).strip()
        return {
            'accion': 'musica',
            'cancion': contenido,
            'artista': 'Artista desconocido'
        }
    
    return None

def extraer_dispositivo(comando):
    """Identifica el dispositivo mencionado en el comando"""
    dispositivos = {
        'luz': ['luz', 'luces', 'iluminación', 'iluminacion', 'lampara', 'lámpara'],
        'ventilador': ['ventilador', 'ventiladores'],
        'calefacción': ['calefacción', 'calefaccion', 'radiador'],
        'aire acondicionado': ['aire acondicionado', 'aire', 'climatizador'],
        'televisor': ['televisor', 'television', 'televisión', 'tv', 'tele'],
        'horno': ['horno'],
        'cafetera': ['cafetera', 'café', 'cafe'],
        'lavadora': ['lavadora'],
        'secadora': ['secadora']
    }
    
    for dispositivo, palabras_clave in dispositivos.items():
        if any(palabra in comando for palabra in palabras_clave):
            return dispositivo
    
    return None

def extraer_ubicacion(comando):
    """Identifica la ubicación mencionada en el comando"""
    ubicaciones = {
        'comedor': ['comedor', 'salon', 'salón'],
        'dormitorio': ['dormitorio', 'habitación', 'habitacion', 'cuarto', 'recámara', 'recamara'],
        'cocina': ['cocina'],
        'baño': ['baño', 'bano', 'aseo'],
        'pasillo': ['pasillo'],
        'entrada': ['entrada', 'recibidor'],
        'garaje': ['garaje', 'garage'],
        'jardín': ['jardín', 'jardin', 'exterior']
    }
    
    for ubicacion, palabras_clave in ubicaciones.items():
        if any(palabra in comando for palabra in palabras_clave):
            return ubicacion
    
    return 'sala principal'  # Ubicación por defecto