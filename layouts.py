from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QSlider
from PyQt6 import QtGui

def create_button(icon_path, tooltip, stylesheet, callback, size=40):
    button = QPushButton("")
    button.setIcon(QtGui.QIcon(icon_path))
    button.setIconSize(QSize(size, size))
    button.setToolTip(tooltip)
    button.setStyleSheet(stylesheet)
    button.clicked.connect(callback)
    return button

def create_left_buttons(main_window):
    left_layout = QVBoxLayout()

    button1 = create_button("images/pivot_gauche", "left side rotation", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid yellow; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("left side rotation"))

    button2 = create_button("images/haut", "up side", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid blue; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("up side"))

    button3 = create_button("images/pivot_droit", "right side rotation", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid pink; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("right side rotation"))

    left_layout_line1 = QHBoxLayout()
    left_layout_line1.addWidget(button1)
    left_layout_line1.addWidget(button2)
    left_layout_line1.addWidget(button3)
    
    container_left_line1 = QWidget()
    container_left_line1.setLayout(left_layout_line1)
    left_layout.addWidget(container_left_line1)

    button4 = create_button("images/gauche", "Left side", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid purple; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("Left side"))

    button5 = create_button("images/centre", "Stop Marty", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid white; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("Stop Marty"))

    button6 = create_button("images/droite", "Right side", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid green; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("Right side"))

    left_layout_line2 = QHBoxLayout()
    left_layout_line2.addWidget(button4)
    left_layout_line2.addWidget(button5)
    left_layout_line2.addWidget(button6)
    
    container_left_line2 = QWidget()
    container_left_line2.setLayout(left_layout_line2)
    left_layout.addWidget(container_left_line2)

    button7 = QLabel("")
    button8 = create_button("images/bas", "Down side", """
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid orange; 
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """, lambda: main_window.on_button_click("Down side"))

    button9 = QLabel("")

    left_layout_line3 = QHBoxLayout()
    left_layout_line3.addWidget(button7)
    left_layout_line3.addWidget(button8)
    left_layout_line3.addWidget(button9)
    
    container_left_line3 = QWidget()
    container_left_line3.setLayout(left_layout_line3)
    left_layout.addWidget(container_left_line3)

    return left_layout
