import tkinter as tk
from tkinter import messagebox
import requests

def download_data_ini(serial_number):
    url = f"http://api.un-click.org/sapd-soft/?serial={serial_number}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        with open("data.ini", "wb") as file:
            file.write(response.content)
        messagebox.showinfo("Éxito", "Archivo data.ini descargado exitosamente.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo descargar el archivo: {e}")

def on_submit():
    serial_number = entry.get()
    if serial_number:
        download_data_ini(serial_number)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número de serie.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Descargador de data.ini")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

label = tk.Label(frame, text="Nº SERIE:")
label.grid(row=0, column=0, pady=5)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, pady=5)

button = tk.Button(frame, text="Descargar", command=on_submit)
button.grid(row=1, columnspan=2, pady=10)

root.mainloop()
