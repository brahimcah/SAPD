import tkinter as tk
import urllib.parse

def generar_url_mailto():
    # Obtener los valores de los campos del formulario
    nombre = nombre_entry.get()
    num_centro = num_centro_entry.get()
    doi = doi_entry.get()
    tipo_centro = tipo_centro_var.get()
    buzon = buzon_entry.get()

    # Crear el mensaje de correo electrónico 
    #El GI-000 ha sido informado por el SAPD que el permiso de conducir DNI/NIE se encuentra en la Jefatura con el número 000
    mensaje = f"Buenos días,\n El {tipo_centro} ha sido informado por el SAPD que el permiso de conducir {doi} se encuentra en la Jefatura con el número {buzon}\nNombre: {nombre}\nNº CENTRO: {num_centro}\nDOI: {doi}\nTipo de Centro: {tipo_centro}"
    
    # Codificar el mensaje y el asunto como parámetros en una URL "mailto"
    body = urllib.parse.quote(mensaje)
    asunto = urllib.parse.quote(f"RECOGIDA PERMISO {nombre} ({doi})")
    mailto_url = f"mailto:crc.jptgi@dgt.es;consulta.jptgi@dgt.es?subject={asunto}&body={body}"

    # Abrir la URL "mailto" en el navegador por defecto
    import webbrowser
    webbrowser.open(mailto_url)

# Crear la ventana principal
root = tk.Tk()

# Crear los campos del formulario
nombre_label = tk.Label(root, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack()

num_centro_label = tk.Label(root, text="Nº CENTRO:")
num_centro_label.pack()
num_centro_entry = tk.Entry(root)
num_centro_entry.pack()

doi_label = tk.Label(root, text="DOI:")
doi_label.pack()
doi_entry = tk.Entry(root)
doi_entry.pack()

buzons = tk.Label(root, text="Buzon:")
buzons.pack()
buzon_entry = tk.Entry(root)
buzon_entry.pack()

# Crear la opción de selección del tipo de centro
tipo_centro_label = tk.Label(root, text="Tipo de Centro:")
tipo_centro_label.pack()
tipo_centro_var = tk.StringVar()
tipo_centro_var.set("-")
tipo_centro_menu = tk.OptionMenu(root, tipo_centro_var, "Centro Médico", "Autoescuela", "Gestoría")
tipo_centro_menu.pack()

# Crear el botón para generar la URL "mailto"
generar_url_boton = tk.Button(root, text="Generar URL", command=generar_url_mailto)
generar_url_boton.pack()

# Iniciar la ventana principal
root.mainloop()
