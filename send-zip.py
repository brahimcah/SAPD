import tkinter as tk
from tkinter import messagebox

# Función para mostrar diferentes cuadros de mensaje
def mostrar_info():
    messagebox.showinfo("Información", "Este es un mensaje de información.")

def mostrar_advertencia():
    messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

def mostrar_error():
    messagebox.showerror("Error", "Este es un mensaje de error.")

def mostrar_pregunta():
    respuesta = messagebox.askquestion("Pregunta", "¿Deseas continuar?")
    if respuesta == 'yes':
        print("El usuario ha decidido continuar.")
    else:
        print("El usuario ha decidido no continuar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Message Box con Iconos")
root.geometry("300x200")

# Botones para mostrar diferentes cuadros de mensaje
boton_info = tk.Button(root, text="Mostrar Información", command=mostrar_info)
boton_info.pack(pady=5)

boton_advertencia = tk.Button(root, text="Mostrar Advertencia", command=mostrar_advertencia)
boton_advertencia.pack(pady=5)

boton_error = tk.Button(root, text="Mostrar Error", command=mostrar_error)
boton_error.pack(pady=5)

boton_pregunta = tk.Button(root, text="Mostrar Pregunta", command=mostrar_pregunta)
boton_pregunta.pack(pady=5)

# Iniciar el bucle principal de la interfaz
root.mainloop()
