import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
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
        mensaje = f"Buenos días,\n hemos sido informado por el SAPD que el permiso de conducir con DOI: {doi} se encuentra en la Jefatura con el número {buzon}\n\nNombre y Apellidos: {nombre}\nNº CENTRO: {num_centro}\nDOI: {doi}\n Fecha de Nacimiento: {year_of_birth}\n Un Saludo"
        
        # Codificar el mensaje y el asunto como parámetros en una URL "mailto"
        body = urllib.parse.quote(mensaje)
        asunto = urllib.parse.quote(f"RECOGIDA PERMISO {doi} ({nombre})")
        mailto_url = f"mailto:crc.jptgi@dgt.es?subject={asunto}&body={body}"

        # Abrir la URL "mailto" en el navegador por defecto
        import webbrowser
        webbrowser.open(mailto_url)
    else:
        # Mostrar un mensaje de error si algún campo está vacío
        messagebox.showerror("Error", "Por favor, complete todos los campos del formulario.")

# Crear la ventana principal
root = tk.Tk()
root.title("Solicitar Recogida")

# Crear y organizar los campos del formulario usando grid
campos = [
    ("Nombre y Apellidos:", 0, 0),
    ("Nº CENTRO:", 1, 0),
    ("DOI:", 2, 0),
    ("Buzon:", 3, 0),
    ("Fecha de Nacimiento:", 4, 0)
]

for label_text, row, col in campos:
    label = tk.Label(root, text=label_text)
    label.grid(row=row, column=col, sticky="w", padx=10, pady=5)

nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1, padx=10, pady=5)

num_centro_entry = tk.Entry(root)
num_centro_entry.grid(row=1, column=1, padx=10, pady=5)

doi_entry = tk.Entry(root)
doi_entry.grid(row=2, column=1, padx=10, pady=5)

buzon_entry = tk.Entry(root)
buzon_entry.grid(row=3, column=1, padx=10, pady=5)

# Crear un widget DateEntry
year_entry = DateEntry(root, width=12, background='darkblue',
                       foreground='white', borderwidth=2, year=2024)
year_entry.grid(row=4, column=1, padx=10, pady=5)

generar_url_boton = tk.Button(root, text="Generar URL", command=generar_url_mailto)
generar_url_boton.grid(row=5, column=0, columnspan=2, pady=10)


# Ajustar el tamaño de las columnas
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

# Iniciar la ventana principal
root.mainloop()
