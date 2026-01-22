import sys
from parser import interpretar_comando

def main():
    print("--- Asistente Domótico ---")
    print("Escribe 'salir' para terminar.")
    
    if len(sys.argv) > 1:
        # Mode batch/test if passing a file
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        print(f"> {line}")
                        interpretar_comando(line)
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado.")
    else:
        # Interactive mode
        while True:
            try:
                comando = input("Entrada: ")
                if comando.lower() in ["salir", "exit"]:
                    break
                interpretar_comando(comando)
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    main()
