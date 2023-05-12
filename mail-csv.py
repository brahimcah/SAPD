import tkinter as tk
import os
import subprocess

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("SAPD")

        self.frame = tk.Frame(master, bg="#333")
        self.frame.pack(expand=True, fill="both")

        self.label = tk.Label(self.frame, text="Seleciona la opción:", fg="#fff", bg="#333", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button_a = tk.Button(self.frame, text="ENVIOS SAPD CSV-ZIP", fg="#fff", bg="#118de6", font=("Helvetica", 12), width=20, height=3, command=self.ejecutar_a)
        self.button_a.pack(pady=10)

        self.button_b = tk.Button(self.frame, text="SOLICITAR PERMISO", fg="#fff", bg="#30a41b", font=("Helvetica", 12), width=20, height=3, command=self.ejecutar_b)
        self.button_b.pack(pady=10)

        self.button_c = tk.Button(self.frame, text="SOPORTE", fg="#fff", bg="#ff0808", font=("Helvetica", 12), width=20, height=3, command=self.ejecutar_c)
        self.button_c.pack(pady=10)

        self.button_salir = tk.Button(self.frame, text="Salir", fg="#fff", bg="#333", font=("Helvetica", 12), width=20, height=3, command=master.quit)
        self.button_salir.pack(pady=10)

        self.label = tk.Label(self.frame, text="Versión: 2.0 - 10/05/2023", fg="#fff", bg="#333", font=("Helvetica", 11))
        self.label.pack(pady=20)

    def ejecutar_a(self):
        subprocess.run(['python', 'sapd-send.py'])

    def ejecutar_b(self):
        subprocess.run(['python', 'perm.py'])


    def ejecutar_c(self):
        subprocess.run(['python', 'soporte.py'])


root = tk.Tk()
menu = Menu(root)
root.mainloop()
