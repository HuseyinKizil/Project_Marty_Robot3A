import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import *



class GameWindows(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Marty Interface")
        self.setGeometry(0,0,500,300)
       
        
        self.start_button = QPushButton("Commencer")
        self.start_button.clicked.connect(self.show_game_windows)
        
        self.quick_button = QPushButton("Quitter")
        self.setCentralWidget(self.start_button)
        self.setCentralWidget(self.quick_button)
        
    def show_game_windows(self,checked):
        self.w = GameWindows()
        self.w.show()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()