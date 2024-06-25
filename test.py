import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os
import glob
import random
import shutil

import tkinter as tk
from tkinter import messagebox

# Obtener el directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir las rutas relativas
soft_dir = os.path.join(current_dir, 'soft')
zip_dir = os.path.join(current_dir, 'zip')

# Verificar si hay archivos en la carpeta 'zip'
if os.path.exists(zip_dir) and os.path.isdir(zip_dir):
    # Encontrar todos los archivos .zip en la carpeta
    zip_files = glob.glob(os.path.join(zip_dir, '*.zip'))
    
    if zip_files:
        # Obtener el archivo .zip más reciente
        latest_zip = max(zip_files, key=os.path.getmtime)
        print("El archivo .zip más reciente es:", latest_zip)
    else:
        messagebox.showwarning("Advertencia", "No se observa ningun fichero SAPD generado")
else:
        messagebox.showwarning("Advertencia", "Error Systema: CZ01 - Contacte con el Administrador sapd@un-click.org")

# Generar un número aleatorio y modificar el nombre del archivo adjunto
random_number = random.randint(1000, 9999)
attachment_filename = f"{os.path.splitext(os.path.basename(latest_zip))[0]}_{random_number}.zip"

# Configuración del servidor SMTP
smtp_host = 'mail.un-click.org'  # Cambia esto por tu servidor SMTP
smtp_port = 465
smtp_user = 'noreply@un-click.org'  # Cambia esto por tu dirección de correo electrónico
smtp_pass = 'PWGceWQ&gSwB'  # Cambia esto por tu contraseña

# Configurar destinatario, remitente, asunto y mensaje
from_email = 'noreply@un-click.org'
from_name = 'GESTOR SAPD'
to_email = 'brahimcah@gmail.com'
subject = 'Archivo SAPD - ' + attachment_filename
body = 'Buenos días,\nSe adjunta el archivo ZIP gestionado por el Gestor SAPD. \n\nAtentamente,\nGestor SAPD \n\n ** Mensaje Enviado des de SAPD-SOFT-AUTH **'
attachment_path = latest_zip  # Cambia esto por la ruta a tu archivo ZIP



# Crear el objeto del mensaje
msg = MIMEMultipart()
msg['From'] = f'{from_name} <{from_email}>'
msg['To'] = to_email
msg['Subject'] = subject

# Adjuntar el cuerpo del mensaje
msg.attach(MIMEText(body, 'plain'))


# Adjuntar el archivo
with open(attachment_path, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={attachment_filename}')
    msg.attach(part)

# Conectarse al servidor SMTP y enviar el correo
try:
    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    server.login(smtp_user, smtp_pass)
    server.send_message(msg)
    messagebox.showinfo("Información", "El archivo se ha enviado con éxito")

    # Directorio de destino
    destination_directory = 'zip/enviados'

    # Asegurarse de que el directorio de destino exista
    os.makedirs(destination_directory, exist_ok=True)

    # Nombre del archivo
    file_name = os.path.basename(attachment_path)

    # Ruta completa del destino
    destination_path = os.path.join(destination_directory, file_name)

    # Mover el archivo
    shutil.move(attachment_path, destination_path)
    print(attachment_path)

finally:
    server.quit()
