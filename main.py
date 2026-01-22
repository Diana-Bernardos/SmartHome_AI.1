"""
Asistente Domótico Simulado
Archivo principal que gestiona la interfaz de usuario y coordina el sistema
"""

from parser import interpretar_comando
from acciones import ejecutar_accion

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del sistema"""
    print("=" * 60)
    print("  ASISTENTE DOMÓTICO - Sistema de Control por Voz")
    print("=" * 60)
    print("\nEjemplos de comandos:")
    print("  - enciende la luz del comedor")
    print("  - apaga el ventilador del dormitorio")
    print("  - pon la calefacción a 22 grados")
    print("  - reproduce Never Gonna Give You Up de Rick Astley")
    print("\nEscribe 'salir' para terminar el programa\n")

def main():
    """Función principal del asistente domótico"""
    mostrar_bienvenida()
    
    while True:
        try:
            # Solicitar comando al usuario
            comando = input("🏠 Comando > ").strip()
            
            # Verificar si el usuario quiere salir
            if comando.lower() in ['salir', 'exit', 'quit']:
                print("\n👋 Cerrando asistente domótico. ¡Hasta pronto!")
                break
            
            # Ignorar entradas vacías
            if not comando:
                continue
            
            # Interpretar el comando ingresado
            accion_parseada = interpretar_comando(comando)
            
            # Ejecutar la acción interpretada
            if accion_parseada:
                resultado = ejecutar_accion(accion_parseada)
                print(f"✓ {resultado}\n")
            else:
                print("❌ No he podido entender ese comando. Intenta reformularlo.\n")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido. ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}\n")

if __name__ == "__main__":
    main()