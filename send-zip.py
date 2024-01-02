import os
import zipfile
import smtplib

def send_zip(email, password, zip_file):
    # Crear un objeto de conexión SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Autenticar con el servidor
    server.login(email, password)

    # Crear un mensaje de correo electrónico
    subject = "PermDev ZIP"
    body = "El ZIP más reciente de PermDev"
    msg = f"Subject: {subject}\n\n{body}"

    # Adjuntar el archivo ZIP
    with open(zip_file, "rb") as f:
        attachment = f.read()
    msg += f"attachment; filename={os.path.basename(zip_file)}"

    # Enviar el correo electrónico
    server.sendmail(email, email, msg.encode())

    server.quit()


if __name__ == "__main__":
    # Obtener la carpeta PermDev
    permdev_dir = "c:\permdev"

    # Obtener el archivo ZIP más reciente
    zip_files = os.listdir(permdev_dir)
    zip_file = max(zip_files, key=lambda f: os.path.getmtime(os.path.join(permdev_dir, f)))

    # Enviar el archivo ZIP
    send_zip("brahimcah@gmail.com", "brahim41581011-R", os.path.join(permdev_dir, zip_file))
