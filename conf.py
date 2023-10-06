# Importar la biblioteca tkinter para la interfaz gráfica
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

# Función para modificar y guardar el archivo seleccionado
def modificar_y_guardar(archivo):
    try:
        # Abrir el archivo en modo escritura
        with open(archivo, 'w') as f:
            # Obtener el contenido del cuadro de texto
            contenido = texto.get(1.0, tk.END)
            # Escribir el contenido en el archivo
            f.write(contenido)
        messagebox.showinfo("Éxito", "Archivo modificado y guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Función para manejar la opción de modificar y guardar el archivo mail
def modificar_mail():
    archivo_mail = filedialog.askopenfilename(title="Seleccionar archivo mail")
    if archivo_mail:
        # Establecer el nombre del archivo en la etiqueta
        archivo_label.config(text=f"Archivo seleccionado: {os.path.basename(archivo_mail)}")
        # Llamar a la función para modificar y guardar el archivo
        modificar_y_guardar(archivo_mail)

# Función para manejar la opción de modificar y guardar el archivo mailcrc
def modificar_mailcrc():
    archivo_mailcrc = filedialog.askopenfilename(title="Seleccionar archivo mailcrc")
    if archivo_mailcrc:
        # Establecer el nombre del archivo en la etiqueta
        archivo_label.config(text=f"Archivo seleccionado: {os.path.basename(archivo_mailcrc)}")
        # Llamar a la función para modificar y guardar el archivo
        modificar_y_guardar(archivo_mailcrc)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Modificar y Guardar Archivos")

# Crear un cuadro de texto
texto = tk.Text(ventana, height=10, width=50)
texto.pack(padx=20, pady=20)

# Crear etiqueta para mostrar el archivo seleccionado
archivo_label = tk.Label(ventana, text="Archivo seleccionado: Ninguno")
archivo_label.pack()

# Crear botones para las opciones
boton_mail = tk.Button(ventana, text="Modificar y Guardar archivo mail", command=modificar_mail)
boton_mail.pack(pady=10)

boton_mailcrc = tk.Button(ventana, text="Modificar y Guardar archivo mailcrc", command=modificar_mailcrc)
boton_mailcrc.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
