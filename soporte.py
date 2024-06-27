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
        self.setWindowTitle('Visor Web Corporativo')
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
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        self.setPalette(palette)

        # Hoja de estilo personalizada
        self.setStyleSheet("""
            QMainWindow {
                background-color: #353535;
            }
            QPushButton {
                background-color: #2D2D2D;
                color: white;
                border: 1px solid #555555;
                padding: 5px 10px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #5A5A5A;
                border: 1px solid #777777;
            }
            QPushButton:pressed {
                background-color: #1C1C1C;
                border: 1px solid #333333;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = WebViewer()
    sys.exit(app.exec_())
