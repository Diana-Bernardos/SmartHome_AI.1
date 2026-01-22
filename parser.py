import re
from acciones import EncenderDispositivo, ApagarDispositivo, AjustarTemperatura, ReproducirMusica

def interpretar_comando(comando):
    comando = comando.lower().strip()
    
    # Caso 7: Reproducir música "pon [cancion] de [artista]"
    # Ejemplo: "pon never gonna give you up de rick astley"
    match_musica = re.search(r"pon (.+) de (.+)", comando)
    if match_musica:
        cancion = match_musica.group(1).strip()
        artista = match_musica.group(2).strip()
        ReproducirMusica(artista, cancion)
        return

    # Caso 5 & 6: Temperatura "pon la [modo] a [temp] grados", "enciende el [modo] a [temp] grados"
    # Ejemplo: "pon la calefacción a 22 grados", "enciende el aire acondicionado a 19 grados"
    match_temp = re.search(r"(?:pon|enciende|ajusta) (?:la|el) (calefacción|aire acondicionado) a (\d+)(?: grados)?", comando)
    if match_temp:
        modo = match_temp.group(1)
        temperatura = match_temp.group(2)
        AjustarTemperatura(modo, temperatura)
        return

    # Caso 1, 2, 3, 4: Encender/Apagar dispositivos
    
    # Ordenar verbos por longitud descendente para evitar coincidencias parciales (ej. "activa" dentro de "activar")
    verbos_encender = ["encender", "enciende", "activar", "activa", "conecta"]
    verbos_apagar = ["desconecta", "desconectar", "desactiva", "desactivar", "apaga", "apagar"]
    
    accion = None
    # Verificar apagar PRIMERO para que "desconecta" no coincida con "conecta"
    if any(v in comando for v in verbos_apagar):
        accion = "apagar"
    elif any(v in comando for v in verbos_encender):
        accion = "encender"
        
    if accion:
        # Intentar extraer ubicación con "del" o "en"
        ubicacion = ""
        dispositivo = ""
        
        # Identificar separadores de ubicacion
        separadores = [" del ", " en ", " de la ", " en la ", " en el ", " de "]
        found_sep = None
        for sep in separadores:
            if sep in comando:
                found_sep = sep
                break
        
        parte_disp = comando
        if found_sep:
            partes = comando.split(found_sep, 1) # Split solo en la primera coincidencia
            parte_disp = partes[0]
            ubicacion = partes[1].strip()
            
            # Limpieza básica de artículos en ubicación
            if ubicacion.startswith("el "): ubicacion = ubicacion[3:]
            if ubicacion.startswith("la "): ubicacion = ubicacion[3:]
            if ubicacion.startswith("las "): ubicacion = ubicacion[4:]
            if ubicacion.startswith("los "): ubicacion = ubicacion[4:]

        # Limpiar verbo y artículos del dispositivo
        # Usamos regex para reemplazar el verbo exacto al inicio
        all_verbs = sorted(verbos_encender + verbos_apagar, key=len, reverse=True)
        for v in all_verbs:
            if parte_disp.startswith(v):
                parte_disp = parte_disp[len(v):].strip()
                break # Solo removemos el primer verbo encontrado
        
        # Limpiar articulos iniciales
        for art in ["el ", "la ", "los ", "las "]:
            if parte_disp.startswith(art):
                parte_disp = parte_disp[len(art):].strip()
                break
        
        dispositivo = parte_disp

        if accion == "encender":
            EncenderDispositivo(ubicacion, dispositivo)
        else:
            ApagarDispositivo(ubicacion, dispositivo)
        return

    print("Comando no reconocido.")
