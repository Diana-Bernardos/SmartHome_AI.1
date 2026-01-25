"""
Módulo de acciones del asistente domótico
Contiene las funciones que ejecutan las acciones físicas simuladas
"""

def EncenderDispositivo(ubicacion, dispositivo):
    """
    Simula el encendido de un dispositivo en una ubicación específica
    
    Args:
        ubicacion (str): Lugar donde se encuentra el dispositivo
        dispositivo (str): Tipo de dispositivo a encender
    
    Returns:
        str: Mensaje de confirmación
    """
    return f"✅ Encendiendo {dispositivo} en {ubicacion}."

def ApagarDispositivo(ubicacion, dispositivo):
    """
    Simula el apagado de un dispositivo en una ubicación específica
    
    Args:
        ubicacion (str): Lugar donde se encuentra el dispositivo
        dispositivo (str): Tipo de dispositivo a apagar
    
    Returns:
        str: Mensaje de confirmación
    """
    return f"✅ Apagando {dispositivo} en {ubicacion}."

def AjustarTemperatura(modo, temperatura):
    """
    Simula el ajuste de temperatura de un sistema de climatización
    
    Args:
        modo (str): Tipo de sistema (calefacción o aire acondicionado)
        temperatura (int): Temperatura deseada en grados Celsius
    
    Returns:
        str: Mensaje de confirmación
    """
    return f"🌡️ Ajustando {modo} a {temperatura}°C."

def ReproducirMusica(artista, cancion):
    """
    Simula la reproducción de una canción
    
    Args:
        artista (str): Nombre del artista
        cancion (str): Título de la canción
    
    Returns:
        str: Mensaje de confirmación
    """
    return f"🎵 Reproduciendo '{cancion}' de {artista}."

def ejecutar_accion(accion_parseada):
    """
    Ejecuta la acción correspondiente según el comando parseado
    
    Args:
        accion_parseada (dict): Diccionario con la acción y parámetros
    
    Returns:
        str: Resultado de la ejecución
    """
    if accion_parseada is None:
        return "❌ No se pudo interpretar el comando."
    
    tipo_accion = accion_parseada.get('accion')
    
    # Manejar comandos no domóticos
    if tipo_accion == 'desconocida':
        return "💡 Solo puedo ayudarte con comandos domóticos. Escribe 'ayuda' para ver ejemplos."
    
    if tipo_accion == 'encender':
        dispositivo = accion_parseada.get('dispositivo') or 'dispositivo'
        ubicacion = accion_parseada.get('ubicacion') or 'sala principal'
        return EncenderDispositivo(ubicacion, dispositivo)
    
    elif tipo_accion == 'apagar':
        dispositivo = accion_parseada.get('dispositivo') or 'dispositivo'
        ubicacion = accion_parseada.get('ubicacion') or 'sala principal'
        return ApagarDispositivo(ubicacion, dispositivo)
    
    elif tipo_accion == 'temperatura':
        modo = accion_parseada.get('modo') or 'climatización'
        temperatura = accion_parseada.get('temperatura') or 20
        return AjustarTemperatura(modo, temperatura)
    
    elif tipo_accion == 'musica':
        artista = accion_parseada.get('artista') or 'Artista desconocido'
        cancion = accion_parseada.get('cancion') or 'Canción desconocida'
        return ReproducirMusica(artista, cancion)
    
    else:
        return "❌ Acción no reconocida."

def ejecutar_accion(accion_parseada):
    """
    Ejecuta la acción correspondiente según el comando parseado
    
    Args:
        accion_parseada (dict): Diccionario con la acción y parámetros
    
    Returns:
        str: Resultado de la ejecución
    """
    if accion_parseada is None:
        return "Error: No se pudo interpretar el comando."
    
    tipo_accion = accion_parseada.get('accion')
    
    if tipo_accion == 'encender':
        dispositivo = accion_parseada.get('dispositivo') or 'dispositivo'
        ubicacion = accion_parseada.get('ubicacion') or 'sala principal'
        return EncenderDispositivo(ubicacion, dispositivo)
    
    elif tipo_accion == 'apagar':
        dispositivo = accion_parseada.get('dispositivo') or 'dispositivo'
        ubicacion = accion_parseada.get('ubicacion') or 'sala principal'
        return ApagarDispositivo(ubicacion, dispositivo)
    
    elif tipo_accion == 'temperatura':
        modo = accion_parseada.get('modo') or 'climatización'
        temperatura = accion_parseada.get('temperatura') or 20
        return AjustarTemperatura(modo, temperatura)
    
    elif tipo_accion == 'musica':
        artista = accion_parseada.get('artista') or 'Artista desconocido'
        cancion = accion_parseada.get('cancion') or 'Canción desconocida'
        return ReproducirMusica(artista, cancion)
    
    else:
        return "Error: Acción no reconocida."