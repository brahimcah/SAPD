import tkinter as tk
import subprocess
from os import system

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("SAPD")
        master.geometry("500x620")  # Define el tamaño de la ventana principal

        # Colores
        bg_color = "#333"
        label_fg_color = "#fff"
        button_fg_color = "#fff"
        button_bg_color = {
            "a": "#118de6",
            "b": "#30a41b",
            "c": "#ff0808",
            "d": "#5dc1b9",
            "salir": bg_color,
        }

        self.frame = tk.Frame(master, bg=bg_color)
        self.frame.pack(expand=True, fill="both")

        # Crear etiqueta de selección
        self.label = tk.Label(self.frame, text="SISTEMA AUTOMATIZADO \n DE PERMISOS DEVUELTOS ", fg=label_fg_color, bg=bg_color, font=("Helvetica", 16))
        self.label.pack(pady=30)

        # Botones en un diccionario para facilitar su creación y gestión
        buttons = {
            "a": ("ENVIOS DATOS SAPD", 20, 3, self.ejecutar_a),
            "b": ("SOLICITAR PERMISO JPT", 20, 3, self.ejecutar_b),
            "c": ("SOPORTE", 20, 3, self.ejecutar_c),
            "d": ("AJUSTES", 20, 3, self.ejecutar_d),
            "salir": ("Salir", 20, 3, master.quit),
        }

        for key, (text, width, height, command) in buttons.items():
            button = tk.Button(self.frame, text=text, fg=button_fg_color, bg=button_bg_color.get(key, None),
                               font=("Helvetica", 12), width=width, height=height, command=command)
            button.pack(pady=10)

        # Etiqueta de versión
        self.version_label = tk.Label(self.frame, text="Versión: 4.1.1 - 07/10/2023", fg=label_fg_color, bg=bg_color, font=("Helvetica", 11))
        self.version_label.pack(pady=20)

    def ejecutar_a(self):
        subprocess.run(['python', 'sapd-send.py'])

    def ejecutar_b(self):
        subprocess.run(['python', 'perm.py'])


    def ejecutar_c(self):
        subprocess.run(['python', 'soporte.py'])

    def ejecutar_d(self):
        subprocess.run(['python', 'conf.py'])


root = tk.Tk()
menu = Menu(root)
root.mainloop()
