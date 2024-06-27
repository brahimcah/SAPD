import tkinter as tk
import subprocess

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("SAPD")
        master.geometry("500x620")  # Define el tamaño de la ventana principal
        master.configure(bg="#f0f0f0")  # Fondo de la ventana principal

        # Colores
        bg_color = "#f0f0f0"
        frame_color = "#ffffff"
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
                               font=("Helvetica", 12), width=width, height=height, command=command, bd=0, relief="solid")
            button.pack(pady=10)

        # Etiqueta de versión
        self.version_label = tk.Label(self.frame, text="Versión: 4.2.1 - 02/01/2024", fg=label_fg_color, bg=frame_color, font=("Helvetica", 11))
        self.version_label.pack(pady=20)

    def ejecutar_a(self):
        subprocess.run(['python3', 'sapd-send.py'])

    def ejecutar_b(self):
        subprocess.run(['python3', 'perm.py'])

    def ejecutar_c(self):
        subprocess.run(['python3', 'soporte.py'])

    def ejecutar_d(self):
        subprocess.run(['python3', 'conf.py'])


root = tk.Tk()
menu = Menu(root)
root.mainloop()
