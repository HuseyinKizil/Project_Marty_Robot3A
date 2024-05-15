from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Mon application avec coins arrondis")

        button = QPushButton("Mon bouton arrondi", self)
        button.clicked.connect(self.close)
        button.setStyleSheet("border-radius: 10px;")  # Arrondir les coins du bouton

        button.resize(120, 60)
        button.move(160, 180)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
