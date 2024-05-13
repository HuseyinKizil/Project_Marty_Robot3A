import sys

from PyQt6.QtCore import QSize, Qt,QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget,QHBoxLayout,QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
   def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty")
       
        main_layout= QHBoxLayout()

        left_layout= QVBoxLayout()

        left_layout_line1= QHBoxLayout()
        left_layout_line1.addWidget(QPushButton("just click"))
        left_layout_line1.addWidget(QPushButton("hey"))
        left_layout_line1.addWidget(QPushButton("hallo"))
        container_left_line1=QWidget()
        container_left_line1.setLayout(left_layout_line1)
        left_layout.addWidget(container_left_line1)

        
        left_layout_line2= QHBoxLayout()
        left_layout_line2.addWidget(QPushButton("just click"))
        left_layout_line2.addWidget(QPushButton("hey"))
        left_layout_line2.addWidget(QPushButton("hallo"))
        container_left_line2=QWidget()
        container_left_line2.setLayout(left_layout_line2)
        left_layout.addWidget(container_left_line2)

         
        left_layout_line3= QHBoxLayout()
        left_layout_line3.addWidget(QPushButton("just click"))
        container_left_line3=QWidget()
        container_left_line3.setLayout(left_layout_line3)
        left_layout.addWidget(container_left_line3)


        container_left = QWidget()
        container_left.setLayout(left_layout)

        right_layout= QVBoxLayout()

        right_layout_line1= QHBoxLayout()
        right_layout_line1.addWidget(QPushButton("just click"))
        right_layout_line1.addWidget(QPushButton("hey"))
        right_layout_line1.addWidget(QPushButton("hallo"))
        right_layout_line1.addWidget(QPushButton("hallo"))
        container_right_line1=QWidget()
        container_right_line1.setLayout(right_layout_line1)
        right_layout.addWidget(container_right_line1)

        right_layout_line2= QHBoxLayout()
        
        right_layout_line2.addWidget(QPushButton("just click"))
        right_layout_line2.addWidget(QPushButton("hey"))
        right_layout_line2.addWidget(QPushButton("hallo"))
        right_layout_line2.addWidget(QPushButton("hallo"))
        container_right_line2=QWidget()
        container_right_line2.setLayout(right_layout_line2)
        right_layout.addWidget(container_right_line2)

        container_right = QWidget()
        container_right.setLayout(right_layout)

        main_layout.addWidget(container_left)
        main_layout.addWidget(container_right)
        container = QWidget()
        container.setLayout(main_layout)


        # Set the central widget of the Window.
        self.setCentralWidget(container)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
