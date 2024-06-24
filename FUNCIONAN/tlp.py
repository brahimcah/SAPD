import tkinter as tk
from tkinter import ttk, messagebox
import requests
import os
import zipfile

# URLs del servidor PHP
VERSION_URL = 'https://api.un-click.org/sapd/version.php'
DOWNLOAD_URL = 'https://api.un-click.org/sapd/download.php'

# Ruta del archivo de la versión local
LOCAL_VERSION_FILE = '../data/version.txt'

# Carpeta de destino para la instalación
DESTINATION_FOLDER = '../soft'

def get_local_version():
    if os.path.exists(LOCAL_VERSION_FILE):
        with open(LOCAL_VERSION_FILE, 'r') as f:
            return f.read().strip()
    return '0.0.0'

def get_remote_version():
    response = requests.get(VERSION_URL)
    if response.status_code == 200:
        return response.text.strip()
    return None

def download_update(version):
    response = requests.get(DOWNLOAD_URL, params={'version': version})
    if response.status_code == 200:
        with open('update.zip', 'wb') as f:
            f.write(response.content)
        return True
    return False

def install_update():
    if not os.path.exists(DESTINATION_FOLDER):
        os.makedirs(DESTINATION_FOLDER)

    with zipfile.ZipFile('update.zip', 'r') as zip_ref:
        zip_ref.extractall(DESTINATION_FOLDER)
    os.remove('update.zip')
    with open(LOCAL_VERSION_FILE, 'w') as f:
        f.write(get_remote_version())

def check_for_updates():
    local_version = get_local_version()
    remote_version = get_remote_version()

    if remote_version and local_version != remote_version:
        return remote_version
    return None

def update_app():
    remote_version = check_for_updates()
    if remote_version:
        if download_update(remote_version):
            install_update()
            messagebox.showinfo("Actualización", f"Actualizado a la versión {remote_version}")
        else:
            messagebox.showerror("Error", "Error al descargar la actualización")
    else:
        messagebox.showinfo("Actualización", "No hay actualizaciones disponibles")

def create_gui():
    root = tk.Tk()
    root.title("Actualizador de Aplicaciones")

    # Configuración de la interfaz
    root.geometry('400x200')
    root.configure(bg='#f0f0f0')

    # Título
    title_label = ttk.Label(root, text="Actualizador de Aplicaciones", font=("Helvetica", 16))
    title_label.pack(pady=20)

    # Botón de actualización
    update_button = ttk.Button(root, text="Buscar actualizaciones", command=update_app)
    update_button.pack(pady=10)

    # Información de la versión actual
    local_version = get_local_version()
    version_label = ttk.Label(root, text=f"Versión actual: {local_version}", font=("Helvetica", 12))
    version_label.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    create_gui()
