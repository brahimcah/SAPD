import hashlib
import csv
import subprocess

# Función para encriptar una cadena usando el algoritmo MD5
def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Leer el contenido del archivo auto.txt y encriptarlo en MD5
with open("auto.txt", "r") as file:
    auto_content = file.read()
    auto_md5 = md5_hash(auto_content)

# Leer el archivo CSV y procesar cada registro
with open("permisos.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Encriptar el registro actual
        encrypted_data = md5_hash(str(row))

        # Construir la URL con los parámetros auto y doi
        url = f"http://localhost:81/sapd-prob/al.php?auto={auto_md5}&doi={encrypted_data}"

        # Construir el comando CURL
        curl_command = ["curl", url]

        # Ejecutar el comando CURL
        try:
            subprocess.run(curl_command, check=True)
            print("Solicitud enviada correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al enviar la solicitud: {e}")
