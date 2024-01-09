import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def enviar_correo(adjunto, destinatario):
    # Configuración del servidor SMTP
    servidor_smtp = 'mail.un-click.org'
    puerto_smtp = 465
    usuario_smtp = 'noreply@un-click.org'
    contraseña_smtp = 'b41581011-R'

    # Configuración del mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_smtp
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'SAPD AUTO-ENVIO'

    # Cuerpo del mensaje (opcional)
    cuerpo_mensaje = MIMEText('Adjunto encontrarás el último ZIP de la carpeta c:\\permdev\\.')
    mensaje.attach(cuerpo_mensaje)

    # Adjuntar el archivo ZIP al mensaje
    with open(adjunto, 'rb') as archivo_zip:
        adjunto_zip = MIMEApplication(archivo_zip.read(), Name=os.path.basename(adjunto))
        adjunto_zip['Content-Disposition'] = f'attachment; filename={os.path.basename(adjunto)}'
        mensaje.attach(adjunto_zip)

    # Iniciar sesión en el servidor SMTP y enviar el correo
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
        servidor.starttls()
        servidor.login(usuario_smtp, contraseña_smtp)
        servidor.send_message(mensaje)

if __name__ == "__main__":
    # Directorio de la carpeta c:\permdev\
    directorio = r'C:\\permdev'

    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(directorio)

    # Filtrar solo los archivos con extensión ZIP
    archivos_zip = [archivo for archivo in archivos if archivo.lower().endswith('.zip')]

    if not archivos_zip:
        print("No se encontraron archivos ZIP en la carpeta.")
    else:
        # Seleccionar el último archivo ZIP
        ultimo_zip = max(archivos_zip, key=lambda f: os.path.getctime(os.path.join(directorio, f)))
        ruta_ultimo_zip = os.path.join(directorio, ultimo_zip)

        # Correo destinatario
        destinatario_correo = 'brahimcah@gmail.com'

        # Enviar el correo con el último ZIP adjunto
        enviar_correo(ruta_ultimo_zip, destinatario_correo)
        print(f"Correo enviado con éxito a {destinatario_correo} con el archivo adjunto: {ultimo_zip}")
