def leer_archivo():
    ruta_archivo = "manejador_archivos/archivo.txt"  # Ruta del archivo dentro de la carpeta manejador_archivos

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return None

def escribir_archivo(texto):
    ruta_archivo = "manejador_archivos/archivo.txt"  # Ruta del archivo dentro de la carpeta manejador_archivos

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

def anexar_archivo(texto):
    ruta_archivo = "manejador_archivos/archivo.txt"  # Ruta del archivo dentro de la carpeta manejador_archivos

    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")