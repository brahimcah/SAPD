import tkinter as tk
import subprocess

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("SAPD")
        master.geometry("400x550")  # Define el tamaño de la ventana principal
        master.configure(bg="#ffffff")  # Fondo de la ventana principal

        # Colores
        bg_color = "#ffffff"
        frame_color = "#f7f7f7"
        label_fg_color = "#333333"
        button_fg_color = "#ffffff"
        button_bg_color = {
            "a": "#007bff",
            "b": "#28a745",
            "c": "#dc3545",
            "d": "#17a2b8",
            "salir": "#6c757d",
        }

        self.frame = tk.Frame(master, bg=frame_color, bd=2, relief="groove")
        self.frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Crear etiqueta de selección
        self.label = tk.Label(self.frame, text="SISTEMA AUTOMATIZADO\nDE PERMISOS DEVUELTOS", fg=label_fg_color, bg=frame_color, font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        # Botones en un diccionario para facilitar su creación y gestión
        buttons = {
            "a": ("ENVIOS DATOS SAPD", self.ejecutar_a),
            "b": ("SOLICITAR PERMISO JPT", self.ejecutar_b),
            "c": ("SOPORTE", self.ejecutar_c),
            "d": ("AJUSTES", self.ejecutar_d),
            "salir": ("Salir", master.quit),
        }

        for key, (text, command) in buttons.items():
            button = tk.Button(self.frame, text=text, fg=button_fg_color, bg=button_bg_color[key],
                               font=("Helvetica", 12), width=30, height=2, command=command, bd=0, relief="solid")
            button.pack(pady=10)

        # Etiqueta de versión
        self.version_label = tk.Label(self.frame, text="Versión: 4.2.1 - 02/01/2024", fg=label_fg_color, bg=frame_color, font=("Helvetica", 10))
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
