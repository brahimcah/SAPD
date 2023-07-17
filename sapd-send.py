import sys
if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import messagebox
else:
    import Tkinter as tk
    import tkMessageBox as messagebox
import csv
import zipfile
from datetime import datetime
import webbrowser
from os import system

archivo = open("mail")
mailsend = archivo.read()
print(mailsend)
archivo.close()


def compra():
    now = datetime.now()
    format = now.strftime('%d%m%Y%H%M%S')
    print(format)

    url_guarda = "C:\permdev\\" + format + ".zip"

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
    mailito = "C:\permdev"
    webbrowser.open(mailito)


class FormWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('500x500')
        self.master.title('Formulario ')
        self.pack()
        self.create_widgets()

        # Load previously entered data (except DOI)
        self.load_data()

    def create_widgets(self):
        # Email fields
        self.email1_label = tk.Label(self, text='Email 1:')
        self.email1_label.pack()
        self.email1_entry = tk.Entry(self)
        self.email1_entry.pack()

        self.email2_label = tk.Label(self, text='Email 2:')
        self.email2_label.pack()
        self.email2_entry = tk.Entry(self)
        self.email2_entry.pack()

        # String field
        self.string_label = tk.Label(self, text='CODIGO CENTRO (EX: GE0000)')
        self.string_label.pack()
        self.string_entry = tk.Entry(self)
        self.string_entry.pack()

        # Multiple cell fields
        self.cell_label = tk.Label(self, text='DOI')
        self.cell_label.pack()
        self.cell_entry = tk.Text(self, height=10)
        self.cell_entry.pack()

        # Button to generate CSV
        self.generate_csv_button = tk.Button(self, text='Enviar datos CSV', command=self.generate_csv)
        self.generate_csv_button.pack()

        # Button to clear DOI field
        self.clear_doi_button = tk.Button(self, text='Limpiar DOI', command=self.clear_doi)
        self.clear_doi_button.pack()

    def reclam(self):
        system("perm.py")

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

        file = open("mail.txt", "w")
        # Comprobamos si el mail2 está rellenado o no
        if not email2:
            mailstotal = email1
        else:
            mailstotal = email1 + ";" + email2
        file.write(mailstotal)
        file.close()

        file = open("auto.txt", "w")
        file.write(string)
        file.close()

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

    def destroy(self):
        self.save_data()
        super().destroy()


root = tk.Tk()
form_window = FormWindow(root)
form_window.mainloop()
