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
    mensaje = f"OK. Encendiendo {dispositivo} en {ubicacion}."
    return mensaje

def ApagarDispositivo(ubicacion, dispositivo):
    """
    Simula el apagado de un dispositivo en una ubicación específica
    
    Args:
        ubicacion (str): Lugar donde se encuentra el dispositivo
        dispositivo (str): Tipo de dispositivo a apagar
    
    Returns:
        str: Mensaje de confirmación
    """
    mensaje = f"OK. Apagando {dispositivo} en {ubicacion}."
    return mensaje

def AjustarTemperatura(modo, temperatura):
    """
    Simula el ajuste de temperatura de un sistema de climatización
    
    Args:
        modo (str): Tipo de sistema (calefacción o aire acondicionado)
        temperatura (int): Temperatura deseada en grados Celsius
    
    Returns:
        str: Mensaje de confirmación
    """
    mensaje = f"OK. Ajustando {modo} a {temperatura} grados."
    return mensaje

def ReproducirMusica(artista, cancion):
    """
    Simula la reproducción de una canción
    
    Args:
        artista (str): Nombre del artista
        cancion (str): Título de la canción
    
    Returns:
        str: Mensaje de confirmación
    """
    mensaje = f"OK. Reproduciendo '{cancion}' de {artista}."
    return mensaje

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
        return EncenderDispositivo(
            accion_parseada['ubicacion'],
            accion_parseada['dispositivo']
        )
    
    elif tipo_accion == 'apagar':
        return ApagarDispositivo(
            accion_parseada['ubicacion'],
            accion_parseada['dispositivo']
        )
    
    elif tipo_accion == 'temperatura':
        return AjustarTemperatura(
            accion_parseada['modo'],
            accion_parseada['temperatura']
        )
    
    elif tipo_accion == 'musica':
        return ReproducirMusica(
            accion_parseada['artista'],
            accion_parseada['cancion']
        )
    
    else:
        return "Error: Acción no reconocida."