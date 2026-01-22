def EncenderDispositivo(ubicacion, dispositivo):
    if ubicacion:
        print(f"OK. Encendiendo {dispositivo} en {ubicacion}.")
    else:
        print(f"OK. Encendiendo {dispositivo}.")

def ApagarDispositivo(ubicacion, dispositivo):
    if ubicacion:
        print(f"OK. Apagando {dispositivo} en {ubicacion}.")
    else:
        print(f"OK. Apagando {dispositivo}.")

def AjustarTemperatura(modo, temperatura):
    print(f"OK. Ajustando {modo} a {temperatura} grados.")

def ReproducirMusica(artista, cancion):
    print(f"OK. Reproduciendo '{cancion}' de {artista}.")
