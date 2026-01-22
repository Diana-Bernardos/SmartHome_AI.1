# Asistente Domótico

## Descripción del Proyecto
Este es un proyecto de asistente domótico simple desarrollado en Python. Permite al usuario controlar dispositivos simulados, ajustar la temperatura y reproducir música mediante comandos de lenguaje natural.

## Estructura de Archivos

*   **main.py**: Punto de entrada de la aplicación. Maneja el bucle principal o la lectura de archivos de comandos.
*   **acciones.py**: Módulo que contiene las funciones "backend" que ejecutan las acciones (simuladas con prints).
    *   `EncenderDispositivo`
    *   `ApagarDispositivo`
    *   `AjustarTemperatura`
    *   `ReproducirMusica`
*   **parser.py**: Módulo encargado de interpretar el texto del usuario y llamar a la función adecuada de `acciones.py`.
*   **pruebas.txt**: Archivo de texto con una lista de comandos de prueba.

## Cómo ejecutarlo

### Requisitos
*   Python 3 instalado.

### Ejecución Interactiva
Para iniciar el asistente en modo interactivo, ejecuta:

```bash
python main.py
```

Escribe tus comandos cuando aparezca `Entrada:`. Escribe `salir` para cerrar.

### Ejecución de Pruebas
Para ejecutar una lista de comandos desde un archivo:

```bash
python main.py pruebas.txt
```

## Ejemplos de Comandos Soportados
*   "enciende la luz del comedor"
*   "apaga la luz del comedor"
*   "pon la calefacción a 22 grados"
*   "pon Never Gonna Give You Up de Rick Astley"

## Capturas
*(Aquí puedes verificar la salida en tu terminal)*
