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

def create_right_buttons(main_window):
    right_layout = QVBoxLayout()

    button1 = QPushButton("Get ready", main_window)
    button1.setIcon(QtGui.QIcon("images/get_ready"))
    button1.setIconSize(QSize(70, 70))
    button1.setToolTip("Marty is ready")
    button1.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid black;
            border-radius: 10px;
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """)
    button1.clicked.connect(lambda: main_window.on_button_click("Get ready"))

    button2 = QPushButton("Show-off", main_window)
    button2.setIcon(QtGui.QIcon("images/get_ready"))
    button2.setIconSize(QSize(70, 70))
    button2.setToolTip("Marty shows-off")
    button2.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid black;
            border-radius: 10px;
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """)
    button2.clicked.connect(lambda: main_window.on_button_click("Show-off"))

    right_layout_line1 = QHBoxLayout()
    right_layout_line1.addWidget(button1)
    right_layout_line1.addWidget(button2)
    
    container_right_line1 = QWidget()
    container_right_line1.setLayout(right_layout_line1)
    right_layout.addWidget(container_right_line1)

    button3 = QPushButton("Wave-left", main_window)
    button3.setIcon(QtGui.QIcon("images/get_ready"))
    button3.setIconSize(QSize(70, 70))
    button3.setToolTip("Marty Wave-left")
    button3.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid black;
            border-radius: 10px;
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """)
    button3.clicked.connect(lambda: main_window.on_button_click("Wave-left"))

    button4 = QPushButton("Wave-right", main_window)
    button4.setIcon(QtGui.QIcon("images/get_ready"))
    button4.setIconSize(QSize(70, 70))
    button4.setToolTip("Marty Wave-right")
    button4.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            border: 1px solid black;
            border-radius: 10px;
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: white;
        }
    """)
    button4.clicked.connect(lambda: main_window.on_button_click("Wave-right"))

    right_layout_line2 = QHBoxLayout()
    right_layout_line2.addWidget(button3)
    right_layout_line2.addWidget(button4)
    
    container_right_line2 = QWidget()
    container_right_line2.setLayout(right_layout_line2)
    right_layout.addWidget(container_right_line2)

    return right_layout
