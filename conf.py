import tkinter as tk
from tkinter import messagebox

class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajustes")
        
        # Nombre de usuario
        self.label_username = tk.Label(root, text="Nombre de Usuario:")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        
        # Correo electrónico
        self.label_email = tk.Label(root, text="Correo Electrónico:")
        self.label_email.grid(row=1, column=0, padx=10, pady=10)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)
        
        # Contraseña
        self.label_password = tk.Label(root, text="Contraseña:")
        self.label_password.grid(row=2, column=0, padx=10, pady=10)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)
        
        # Notificaciones
        self.label_notifications = tk.Label(root, text="Notificaciones:")
        self.label_notifications.grid(row=3, column=0, padx=10, pady=10)
        self.notifications_var = tk.BooleanVar()
        self.checkbox_notifications = tk.Checkbutton(root, text="Activar", variable=self.notifications_var)
        self.checkbox_notifications.grid(row=3, column=1, padx=10, pady=10)
        
        # Botón de guardar
        self.button_save = tk.Button(root, text="Guardar", command=self.save_settings)
        self.button_save.grid(row=4, column=0, columnspan=2, pady=20)
        
    def save_settings(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        notifications = self.notifications_var.get()
        
        # Aquí puedes agregar lógica para guardar las configuraciones
        print(f"Nombre de Usuario: {username}")
        print(f"Correo Electrónico: {email}")
        print(f"Contraseña: {password}")
        print(f"Notificaciones: {'Activadas' if notifications else 'Desactivadas'}")
        
        # Muestra un mensaje de éxito
        messagebox.showinfo("Ajustes", "Configuraciones guardadas con éxito")

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsWindow(root)
    root.mainloop()
