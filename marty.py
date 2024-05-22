import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import QColor
from martypy import Marty


# Subclass QMainWindow to customize your application's main window
class Game(QMainWindow):
        
        def __init__(self):
                super().__init__()

                self.setWindowTitle("Marty")
                self.setGeometry(0,0,500,300)
                self.setStyleSheet("background-color: cyan")
       
                main_layout= QHBoxLayout()

                left_layout= QVBoxLayout()
    
                left_layout_line1= QHBoxLayout()
                btn_commencer = QPushButton("Commencer",self)
                btn_commencer.setStyleSheet("background-color: green")
                btn_commencer.clicked.connect(self.show_game_windows)
                left_layout_line1.addWidget(btn_commencer)

                container_left_line1=QWidget()
                container_left_line1.setLayout(left_layout_line1)
                left_layout.addWidget(container_left_line1)
         
                left_layout_line2= QHBoxLayout()
                btn_quitter = QPushButton("Quitter",self)
                btn_quitter.setStyleSheet("background-color: red")
                btn_quitter.clicked.connect(self.close)
                left_layout_line2.addWidget(btn_quitter)
                
                container_left_line2=QWidget()
                container_left_line2.setLayout(left_layout_line2)
                left_layout.addWidget(container_left_line2)


                container_left = QWidget()
                container_left.setLayout(left_layout)

                main_layout.addWidget(container_left)
                container = QWidget()
                container.setLayout(main_layout)


                # Set the central widget of the Window.
                self.setCentralWidget(container)

         
        def show_game_windows(self,checked):  
                self.hide()
                my_marry = Marty("wifi", "192.168.0.104")
                my_marry.hello()

                self.w = GameWindows()
                self.w.show()
                

class GameWindows(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(100,100, 500,300)
        

app = QApplication(sys.argv)

window = Game()
window.show()

app.exec()