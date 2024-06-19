import tkinter as tk
import time

# Definir la ventana principal
ventana = tk.Tk()
ventana.title("Pantalla formal")
ventana.geometry("800x600")

# Configurar el estilo formal
ventana.configure(bg="#F0F0F0") # Color de fondo claro
ventana.option_add("-font", "Arial 12") # Fuente formal

# Agregar imagen
imagen = tk.PhotoImage(file="logo.png") # Reemplazar "imagen.png" por la ruta real
etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.pack(pady=20)

# Agregar texto
texto = tk.Label(ventana, text="**Texto formal**", justify="center", font=("Arial", 16, "bold"))
texto.pack(pady=20)

# Cerrar la ventana después de 30 segundos
def cerrar_ventana():
  ventana.destroy()

def actualizacion():
  print()

ventana.after(30000, cerrar_ventana) # 30000 milisegundos = 30 segundos

# Iniciar el bucle principal de la ventana
ventana.mainloop()
