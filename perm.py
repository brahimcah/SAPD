import tkinter as tk
from tkinter import messagebox
import urllib.parse

def generar_url_mailto():
    # Obtener los valores de los campos del formulario
    nombre = nombre_entry.get()
    num_centro = num_centro_entry.get()
    doi = doi_entry.get()
    buzon = buzon_entry.get()
     
    year_of_birth = year_entry.get()

    # Validar que todos los campos estén llenos
    if nombre and num_centro and doi and buzon and year_of_birth:
        # Crear el mensaje de correo electrónico 
        mensaje = f"Buenos días,\n hemos sido informado por el SAPD que el permiso de conducir con DOI: {doi} se encuentra en la Jefatura con el número {buzon}\nNombre: {nombre}\nNº CENTRO: {num_centro}\nDOI: {doi}\nAño de Nacimiento: {year_of_birth}\n Un Saludo"
        
        # Codificar el mensaje y el asunto como parámetros en una URL "mailto"
        body = urllib.parse.quote(mensaje)
        asunto = urllib.parse.quote(f"RECOGIDA PERMISO {nombre} ({doi})")
        mailto_url = f"mailto:crc.jptgi@dgt.es?subject={asunto}&body={body}"

        # Abrir la URL "mailto" en el navegador por defecto
        import webbrowser
        webbrowser.open(mailto_url)
    else:
        # Mostrar un mensaje de error si algún campo está vacío
        messagebox.showerror("Error", "Por favor, complete todos los campos del formulario.")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de URL de Correo Electrónico")

# Crear y organizar los campos del formulario usando grid
nombre_label = tk.Label(root, text="Nombre y Apellidos:")
nombre_label.grid(row=0, column=0, sticky="w")
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

num_centro_label = tk.Label(root, text="Nº CENTRO:")
num_centro_label.grid(row=1, column=0, sticky="w")
num_centro_entry = tk.Entry(root)
num_centro_entry.grid(row=1, column=1)

doi_label = tk.Label(root, text="DOI:")
doi_label.grid(row=2, column=0, sticky="w")
doi_entry = tk.Entry(root)
doi_entry.grid(row=2, column=1)

buzon_label = tk.Label(root, text="Buzon:")
buzon_label.grid(row=3, column=0, sticky="w")
buzon_entry = tk.Entry(root)
buzon_entry.grid(row=3, column=1)

year_label = tk.Label(root, text="Fecha de Nacimiento:")
year_label.grid(row=4, column=0, sticky="w")
year_entry = tk.Entry(root)
year_entry.grid(row=4, column=1)


generar_url_boton = tk.Button(root, text="Generar URL", command=generar_url_mailto)
generar_url_boton.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar la ventana principal
root.mainloop()
