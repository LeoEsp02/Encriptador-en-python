from cryptography.fernet import Fernet

# Generar y guardar una clave (hacer esto una vez)
def generar_clave(nombre_archivo="clave.key"):
    clave = Fernet.generate_key()
    with open(nombre_archivo, "wb") as archivo_clave:
        archivo_clave.write(clave)

# Cargar la clave
def cargar_clave(nombre_archivo="clave.key"):
    with open(nombre_archivo, "rb") as archivo_clave:
        return archivo_clave.read()

# Encriptar un archivo de texto
def encriptar_archivo(ruta_entrada, ruta_salida, clave):
    fernet = Fernet(clave)
    with open(ruta_entrada, "r") as archivo:
        texto = archivo.read().encode()  # Convertir a bytes
    texto_encriptado = fernet.encrypt(texto)
    with open(ruta_salida, "wb") as archivo_encriptado:
        archivo_encriptado.write(texto_encriptado)
    print(f"Archivo encriptado y guardado en {ruta_salida}")

# Desencriptar un archivo de texto
def desencriptar_archivo(ruta_entrada, ruta_salida, clave):
    fernet = Fernet(clave)
    with open(ruta_entrada, "rb") as archivo_encriptado:
        texto_encriptado = archivo_encriptado.read()
    texto_desencriptado = fernet.decrypt(texto_encriptado)
    with open(ruta_salida, "w") as archivo_desencriptado:
        archivo_desencriptado.write(texto_desencriptado.decode())  # Convertir de bytes a texto
    print(f"Archivo desencriptado y guardado en {ruta_salida}")

# Ejecución del programa
if __name__ == "__main__":
    # Generar la clave una vez (descomenta si no tienes una clave generada)
    # generar_clave()

    # Cargar clave existente
    clave = cargar_clave()

    # Encriptar archivo
    encriptar_archivo("archivo_original.txt", "archivo_encriptado.txt", clave)

    # Desencriptar archivo
    desencriptar_archivo("archivo_encriptado.txt", "archivo_desencriptado.txt", clave)
