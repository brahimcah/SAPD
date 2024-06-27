import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SAPD")
        self.setGeometry(100, 100, 400, 550)  # Tamaño de la ventana principal
        self.setStyleSheet("background-color: #ffffff;")

        layout = QVBoxLayout()
        layout.setSpacing(20)  # Espaciado entre widgets

        # Crear etiqueta de selección
        label = QLabel("SISTEMA AUTOMATIZADO\nDE PERMISOS DEVUELTOS")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Helvetica", 16, QFont.Bold))
        label.setStyleSheet("color: #333333;")
        layout.addWidget(label)

        # Botones y sus acciones
        buttons = {
            "ENVIOS DATOS SAPD": self.ejecutar_a,
            "SOLICITAR PERMISO JPT": self.ejecutar_b,
            "SOPORTE": self.ejecutar_c,
            "AJUSTES": self.ejecutar_d,
            "Salir": self.close
        }

        button_styles = """
        QPushButton {
            font: 12pt "Helvetica";
            color: #000000;
            height: 40px;
            border-radius: 5px;
        }
        QPushButton#Salir {
            background-color: #6c757d;
        }
        """

        for text, func in buttons.items():
            button = QPushButton(text)
            button.setObjectName(text.replace(" ", ""))
            button.clicked.connect(func)
            button.setStyleSheet(button_styles + self.get_button_style(text))
            layout.addWidget(button)

        # Etiqueta de versión
        version_label = QLabel("Versión: 4.2.1 - 02/01/2024")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setFont(QFont("Helvetica", 10))
        version_label.setStyleSheet("color: #333333;")
        layout.addWidget(version_label)

        self.setLayout(layout)

    def get_button_style(self, text):
        if "ENVIOS" in text:
            return "background-color: #007bff;"
        elif "PERMISO" in text:
            return "background-color: #a328a7;"
        elif "SOPORTE" in text:
            return "background-color: #dc3545;"
        elif "AJUSTES" in text:
            return "background-color: #17a2b8;"
        else:
            return ""

    def ejecutar_a(self):
        subprocess.run(['python3', 'sapd-send.py'])

    def ejecutar_b(self):
        subprocess.run(['python3', 'perm.py'])

    def ejecutar_c(self):
        subprocess.run(['python3', 'soporte.py'])

    def ejecutar_d(self):
        subprocess.run(['python3', 'conf.py'])

def main():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
