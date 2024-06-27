import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor

import csv
import zipfile
from datetime import datetime
import webbrowser
import os

class FormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulario con Estilo Bootstrap')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icono.png'))  # Reemplaza 'icono.png' con la ruta de tu icono

        self.initUI()
        self.load_data()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Paleta de colores para imitar Bootstrap
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.Text, QColor(51, 51, 51))
        self.setPalette(palette)

        # Estilo de la fuente
        font = QFont('Arial', 12)

        # Títulos para secciones principales
        section_label = QLabel('Formulario de Envío Corporativo')
        section_label.setFont(QFont('Arial', 16, QFont.Bold))
        layout.addWidget(section_label)

        # Email fields
        email_layout = QHBoxLayout()
        layout.addLayout(email_layout)

        self.email1_label = QLabel('Email Principal:')
        self.email1_label.setFont(font)
        self.email1_entry = QLineEdit()
        self.email1_entry.setFont(font)
        email_layout.addWidget(self.email1_label)
        email_layout.addWidget(self.email1_entry)

        self.email2_label = QLabel('Email Secundario:')
        self.email2_label.setFont(font)
        self.email2_entry = QLineEdit()
        self.email2_entry.setFont(font)
        email_layout.addWidget(self.email2_label)
        email_layout.addWidget(self.email2_entry)

        # Campo para código del centro
        string_layout = QHBoxLayout()
        layout.addLayout(string_layout)

        self.string_label = QLabel('Código del Centro:')
        self.string_label.setFont(font)
        self.string_entry = QLineEdit()
        self.string_entry.setFont(font)
        string_layout.addWidget(self.string_label)
        string_layout.addWidget(self.string_entry)

        # Área de texto para DOI
        doi_layout = QVBoxLayout()
        layout.addLayout(doi_layout)

        self.cell_label = QLabel('DOI:')
        self.cell_label.setFont(font)
        doi_layout.addWidget(self.cell_label)

        self.cell_entry = QTextEdit()
        self.cell_entry.setFont(font)
        doi_layout.addWidget(self.cell_entry)

        # Botones
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.generate_csv_button = QPushButton('Generar Archivo CSV')
        self.generate_csv_button.setFont(font)
        self.generate_csv_button.setStyleSheet('QPushButton { background-color: #007bff; color: white; border-radius: 5px; padding: 10px; }'
                                               'QPushButton:hover { background-color: #0056b3; }')
        self.generate_csv_button.clicked.connect(self.generate_csv)
        button_layout.addWidget(self.generate_csv_button)

        self.tvl_button = QPushButton('Envío Telemático')
        self.tvl_button.setFont(font)
        self.tvl_button.setStyleSheet('QPushButton { background-color: #28a745; color: white; border-radius: 5px; padding: 10px; }'
                                      'QPushButton:hover { background-color: #218838; }')
        self.tvl_button.clicked.connect(self.send_telematic)
        button_layout.addWidget(self.tvl_button)

        self.clear_doi_button = QPushButton('Limpiar DOI')
        self.clear_doi_button.setFont(font)
        self.clear_doi_button.setStyleSheet('QPushButton { background-color: #dc3545; color: white; border-radius: 5px; padding: 10px; }'
                                            'QPushButton:hover { background-color: #c82333; }')
        self.clear_doi_button.clicked.connect(self.clear_doi)
        button_layout.addWidget(self.clear_doi_button)

    def generate_csv(self):
        # Obtener valores del formulario
        email1 = self.email1_entry.text()
        email2 = self.email2_entry.text()
        string = self.string_entry.text()
        cells = self.cell_entry.toPlainText()

        # Validar campos
        if not email1 or not string or not cells.strip():
            QMessageBox.critical(self, 'Error', 'Por favor, rellena todos los campos del formulario.')
            return

        with open("mail.txt", "w") as file:
            mailstotal = email1 if not email2 else f"{email1};{email2}"
            file.write(mailstotal)

        with open("auto.txt", "w") as file:
            file.write(string)

        # Crear archivo CSV y escribir datos
        with open('permisos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([cell.strip().split('\t') for cell in cells.split('\n') if cell.strip()])

        QMessageBox.information(self, 'Éxito', 'Archivo CSV generado.')
        self.compra()

    def clear_doi(self):
        self.cell_entry.clear()

    def load_data(self):
        try:
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    self.email1_entry.setText(lines[0].strip())
                    self.email2_entry.setText(lines[1].strip())
                    self.string_entry.setText(lines[2].strip())
        except FileNotFoundError:
            pass

    def save_data(self):
        email1 = self.email1_entry.text()
        email2 = self.email2_entry.text()
        string = self.string_entry.text()

        with open('data.txt', 'w') as file:
            file.write(email1 + '\n')
            file.write(email2 + '\n')
            file.write(string + '\n')

    def compra(self):
        now = datetime.now()
        format = now.strftime('%d%m%Y%H%M%S')

        url_guarda = os.path.join("C:\\permdev", f"{format}.zip")

        try:
            compression = zipfile.ZIP_DEFLATED
        except AttributeError:
            compression = zipfile.ZIP_STORED

        with zipfile.ZipFile(url_guarda, mode="w") as zf:
            zf.write("auto.txt", compress_type=compression)
            zf.write("mail.txt", compress_type=compression)
            zf.write("permisos.csv", compress_type=compression)

        mailito = f"mailto:{self.email1_entry.text()}?&subject=CSV-ZIP PERMISOS DEV&body=Buenos días,%0A te adjunto los datos del programa:%0A%0AUn Saludo"
        webbrowser.open(mailito)
        webbrowser.open("C:\\permdev")

    def send_telematic(self):
        # Aquí implementa la lógica para enviar la información telemáticamente
        QMessageBox.information(self, 'Envío Telemático', 'Funcionalidad aún no implementada.')

    def closeEvent(self, event):
        self.save_data()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(app.exec_())
