import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPalette, QColor

class WebViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SAPD - INCIDENCIAS')
        self.setGeometry(100, 100, 1024, 768)

        # Crear un widget central y un layout vertical
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Crear un widget QWebEngineView
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        # Crear un botón para cerrar la aplicación
        close_button = QPushButton('Cerrar')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setCentralWidget(central_widget)

        # Establecer una URL predeterminada
        self.browser.setUrl(QUrl('https://form.un-click.org/sapd.php'))

        # Aplicar estilo corporativo
        self.applyCorporateStyle()

        self.show()

    def applyCorporateStyle(self):
        # Paleta de colores personalizada
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(245, 245, 245))
        palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(255, 255, 255))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))

        self.setPalette(palette)

        # Hoja de estilo personalizada al estilo Bootstrap
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: 1px solid #007BFF;
                padding: 5px 10px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
                border: 1px solid #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
                border: 1px solid #004085;
            }
            QPushButton:disabled {
                background-color: #6c757d;
                border: 1px solid #6c757d;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = WebViewer()
    sys.exit(app.exec_())
