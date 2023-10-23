import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

# Lista de correos electrónicos y correos electrónicos CRC asociados con cada provincia
correos = {
    "Girona": ["consulta.jptgi@dgt.es", "crc.jptgi@dgt.es"]
}

def modificar_y_guardar(archivo, provincia):
    try:
        with open(archivo, 'w') as f:
            contenido = correos[provincia][0] if "mail" in archivo else correos[provincia][1]
            f.write(contenido)
        messagebox.showinfo("Éxito", f"Archivo {os.path.basename(archivo)} modificado y guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def modificar_mail():
    provincia = provincia_var.get()
    archivo_mail = os.path.join(os.getcwd(), "mail")
    archivo_label.config(text=f"Archivo seleccionado: {os.path.basename(archivo_mail)}")
    modificar_y_guardar(archivo_mail, provincia)

def modificar_mailcrc():
    provincia = provincia_var.get()
    archivo_mailcrc = os.path.join(os.getcwd(), "mailcrc")
    archivo_label.config(text=f"Archivo seleccionado: {os.path.basename(archivo_mailcrc)}")
    modificar_y_guardar(archivo_mailcrc, provincia)

ventana = tk.Tk()
ventana.title("Modificar y Guardar Archivos")

provincias = list(correos.keys())
provincia_var = tk.StringVar(ventana)
provincia_var.set(provincias[0])  # Establecer el valor predeterminado

provincia_menu = tk.OptionMenu(ventana, provincia_var, *provincias)
provincia_menu.pack(padx=20, pady=20)

archivo_label = tk.Label(ventana, text="Archivo seleccionado: Ninguno")
archivo_label.pack()

boton_mail = tk.Button(ventana, text="Modificar y Guardar archivo mail", command=modificar_mail)
boton_mail.pack(pady=10)

boton_mailcrc = tk.Button(ventana, text="Modificar y Guardar archivo mailcrc", command=modificar_mailcrc)
boton_mailcrc.pack(pady=10)

ventana.mainloop()
