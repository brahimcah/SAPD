import tkinter as tk
from tkinter import ttk, messagebox
import csv
import zipfile
from datetime import datetime
import webbrowser
from os import system

archivo = open("mail")
mailsend = archivo.read()
archivo.close()


def compra():
    now = datetime.now()
    format = now.strftime('%d%m%Y%H%M%S')

    url_guarda = "C:\\permdev\\" + format + ".zip"

    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    zf = zipfile.ZipFile(url_guarda, mode="w")
    try:
        zf.write("auto.txt", compress_type=compression)
        zf.write("mail.txt", compress_type=compression)
        zf.write("permisos.csv", compress_type=compression)
    finally:
        zf.close()
    mailito = "mailto:" + mailsend + "?&subject= CSV-ZIP PERMISOS DEV &body= Buenos días, %0A te adjunto los datos del programa: %0A %0A Un Saludo"
    webbrowser.open(mailito)
    mailito = "C:\\permdev"
    webbrowser.open(mailito)


class FormWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Formulario')
        self.geometry('500x500')

        # Create a style
        self.style = ttk.Style(self)

        # Set the theme to a modern theme (e.g., 'clam', 'alt', 'default', 'vista', etc.)
        self.style.theme_use('clam')

        # Configure the style for specific elements
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))

        self.create_widgets()

        # Load previously entered data (except DOI)
        self.load_data()

    def create_widgets(self):
        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)

        # Email fields
        email_frame = ttk.Frame(container)
        email_frame.pack(pady=10)

        self.email1_label = ttk.Label(email_frame, text='Email 1:')
        self.email1_label.pack(side=tk.LEFT, padx=5)
        self.email1_entry = ttk.Entry(email_frame)
        self.email1_entry.pack(side=tk.LEFT, padx=5)

        email2_frame = ttk.Frame(container)
        email2_frame.pack(pady=10)

        self.email2_label = ttk.Label(email2_frame, text='Email 2:')
        self.email2_label.pack(side=tk.LEFT, padx=5)
        self.email2_entry = ttk.Entry(email2_frame)
        self.email2_entry.pack(side=tk.LEFT, padx=5)

        # String field
        string_frame = ttk.Frame(container)
        string_frame.pack(pady=10)

        self.string_label = ttk.Label(string_frame, text='CODIGO CENTRO (EX: GE0000)')
        self.string_label.pack(side=tk.LEFT, padx=5)
        self.string_entry = ttk.Entry(string_frame)
        self.string_entry.pack(side=tk.LEFT, padx=5)

        # Multiple cell fields
        doi_frame = ttk.Frame(container)
        doi_frame.pack(pady=10)

        self.cell_label = ttk.Label(doi_frame, text='DOI')
        self.cell_label.pack(side=tk.LEFT, padx=5)
        self.cell_entry = tk.Text(doi_frame, height=10)
        self.cell_entry.pack(side=tk.LEFT, padx=5)

        # Button to generate CSV
        generate_frame = ttk.Frame(container)
        generate_frame.pack(pady=10)

        self.generate_csv_button = ttk.Button(generate_frame, text='Enviar datos CSV', command=self.generate_csv)
        self.generate_csv_button.pack()

        # Button to clear DOI field
        self.clear_doi_button = ttk.Button(generate_frame, text='Limpiar DOI', command=self.clear_doi)
        self.clear_doi_button.pack()

    def generate_csv(self):
        # Get values from the form
        email1 = self.email1_entry.get()
        email2 = self.email2_entry.get()
        string = self.string_entry.get()
        cells = self.cell_entry.get('1.0', tk.END)

        # Check if any field is empty
        if not email1 or not string or not cells.strip():
            messagebox.showerror('Error', 'Por favor, rellena todos los campos del formulario.')
            return

        with open("mail.txt", "w") as file:
            mailstotal = email1 if not email2 else email1 + ";" + email2
            file.write(mailstotal)

        with open("auto.txt", "w") as file:
            file.write(string)

        # Create CSV file and write data
        with open('permisos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([cell.strip().split('\t') for cell in cells.split('\n')])

        messagebox.showinfo('Éxito', 'Archivo CSV generado.')
        compra()

    def clear_doi(self):
        self.cell_entry.delete('1.0', tk.END)

    def load_data(self):
        try:
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    self.email1_entry.insert(0, lines[0].strip())
                    self.email2_entry.insert(0, lines[1].strip())
                    self.string_entry.insert(0, lines[2].strip())
        except FileNotFoundError:
            pass

    def save_data(self):
        email1 = self.email1_entry.get()
        email2 = self.email2_entry.get()
        string = self.string_entry.get()

        with open('data.txt', 'w') as file:
            file.write(email1 + '\n')
            file.write(email2 + '\n')
            file.write(string + '\n')


app = FormWindow()
app.mainloop()
