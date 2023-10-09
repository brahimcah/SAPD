import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def modificar_y_guardar(archivo):
    try:
        with open(archivo, 'w') as f:
            contenido = texto.get(1.0, tk.END)
            f.write(contenido)
        messagebox.showinfo("Éxito", "Archivo modificado y guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def modificar_mail():
    archivo_mail = os.path.join(os.getcwd(), "mail")
    archivo_label.config(text=f"Archivo seleccionado: {os.path.basename(archivo_mail)}")
    modificar_y_guardar(archivo_mail)

def modificar_mailcrc():
    archivo_mailcrc = os.path.join(os.getcwd(), "mailcrc")
    archivo_label.config(text=f"Archivo seleccionado: {os.path.basename(archivo_mailcrc)}")
    modificar_y_guardar(archivo_mailcrc)

ventana = tk.Tk()
ventana.title("Modificar y Guardar Archivos")

texto = tk.Text(ventana, height=10, width=50)
texto.pack(padx=20, pady=20)

archivo_label = tk.Label(ventana, text="Archivo seleccionado: Ninguno")
archivo_label.pack()

boton_mail = tk.Button(ventana, text="Modificar y Guardar archivo mail", command=modificar_mail)
boton_mail.pack(pady=10)

boton_mailcrc = tk.Button(ventana, text="Modificar y Guardar archivo mailcrc", command=modificar_mailcrc)
boton_mailcrc.pack(pady=10)

ventana.mainloop()
