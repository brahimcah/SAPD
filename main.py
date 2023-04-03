import tkinter as tk
from os import system
from tkinter import filedialog
import zipfile



def open_window2():
    system("del permisos.csv")
    system("del mail.txt")
    system("del auto.txt")
    system("mail-csv.py")

def open_window3():
    system("curl -O https://codeload.github.com/brahimcah/SAPD/zip/refs/heads/main")
    zip_file = filedialog.askopenfilename()
    print(zip_file)
    if zip_file:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall('./datos')
    system("del *zip")


# create main window
main_window = tk.Tk()
main_window.title('SAPD')
main_window.geometry('500x500')

# create buttons
button2 = tk.Button(main_window, text='Generar Avisos de Permisos DGT', command=open_window2)

# add buttons to main window
button1.pack()
button2.pack()
button3.pack()

# start the event loop
main_window.mainloop()
