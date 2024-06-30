import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from qtawesome import icon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Layout principal
        layout = QVBoxLayout()
        
        # Estilo para los botones
        button_style = "QPushButton { font-size: 14px; padding: 10px; margin: 5px; border: 1px solid #ccc; border-radius: 5px; }"
        
        # Botón 1: Ejecutar script 1
        self.btn1 = QPushButton(icon('fa.play-circle', color='green'), 'Ejecutar script 1', self)
        self.btn1.setStyleSheet(button_style)
        self.btn1.clicked.connect(lambda: self.run_script(1))
        layout.addWidget(self.btn1)
        
        # Botón 2: Ejecutar script 2
        self.btn2 = QPushButton(icon('fa.play-circle', color='green'), 'Ejecutar script 2', self)
        self.btn2.setStyleSheet(button_style)
        self.btn2.clicked.connect(lambda: self.run_script(2))
        layout.addWidget(self.btn2)
        
        # Botón 3: Ejecutar script 3
        self.btn3 = QPushButton(icon('fa.play-circle', color='green'), 'Ejecutar script 3', self)
        self.btn3.setStyleSheet(button_style)
        self.btn3.clicked.connect(lambda: self.run_script(3))
        layout.addWidget(self.btn3)
        
        # Botón 4: Ejecutar script 4
        self.btn4 = QPushButton(icon('fa.play-circle', color='green'), 'Ejecutar script 4', self)
        self.btn4.setStyleSheet(button_style)
        self.btn4.clicked.connect(lambda: self.run_script(4))
        layout.addWidget(self.btn4)
        
        # Botón para abrir la ventana de lectura de XML
        self.xmlButton = QPushButton(icon('fa.file-text-o', color='blue'), 'Leer XML', self)
        self.xmlButton.setStyleSheet(button_style)
        self.xmlButton.clicked.connect(self.openXmlWindow)
        layout.addWidget(self.xmlButton)
        
        self.setLayout(layout)
        
        self.setWindowTitle('SAPD - AJUSTES')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    
    def run_script(self, script_number):
        try:
            # Ajusta los nombres de los scripts según tus necesidades
            script_name = f'script{script_number}.py'
            subprocess.run(['python', script_name])
        except Exception as e:
            print(f"Error al ejecutar el script {script_number}: {e}")
    
    def openXmlWindow(self):
        self.xmlWindow = XmlWindow()
        self.xmlWindow.show()

class XmlWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Layout para la ventana de XML
        layout = QVBoxLayout()
        
        # Estilo para los botones
        button_style = "QPushButton { font-size: 14px; padding: 10px; margin: 5px; border: 1px solid #ccc; border-radius: 5px; }"
        
        # Botón para cargar archivo XML
        self.loadButton = QPushButton(icon('fa.folder-open', color='orange'), 'Cargar archivo XML', self)
        self.loadButton.setStyleSheet(button_style)
        self.loadButton.clicked.connect(self.loadXml)
        layout.addWidget(self.loadButton)
        
        # Etiqueta para mostrar el contenido del XML
        self.xmlContent = QLabel('Contenido del XML aparecerá aquí', self)
        self.xmlContent.setAlignment(Qt.AlignTop)
        layout.addWidget(self.xmlContent)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Leer XML')
        self.setGeometry(300, 300, 400, 300)
    
    def loadXml(self):
        # Aquí cargarías el archivo XML desde la carpeta 'data'
        # Debes implementar esta función según tus necesidades
        pass

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
