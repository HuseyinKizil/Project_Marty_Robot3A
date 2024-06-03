from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QSlider
from PyQt6 import QtGui
from martypy import Marty

def create_button(icon_path, tooltip, stylesheet, callback, size=40):
    button = QPushButton("")
    button.setIcon(QtGui.QIcon(icon_path))
    button.setIconSize(QSize(size, size))
    button.setToolTip(tooltip)
    button.setStyleSheet(stylesheet)
    button.clicked.connect(callback)
    return button

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
    button2.clicked.connect(main_window.get_ready)
    
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
    button3.clicked.connect(main_window.wave_left)
    
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
    button4.clicked.connect(main_window.wave_right)

    right_layout_line1 = QHBoxLayout()
    right_layout_line1.addWidget(button1)
    right_layout_line1.addWidget(button2)
    right_layout_line1.addWidget(button3)
    right_layout_line1.addWidget(button4)
    
    container_right_line1 = QWidget()
    container_right_line1.setLayout(right_layout_line1)
    right_layout.addWidget(container_right_line1)

    button5 = QPushButton("Dance", main_window)
    button5.setIcon(QtGui.QIcon("images/get_ready"))
    button5.setIconSize(QSize(70, 70))
    button5.setToolTip("Marty Wave-left")
    button5.setStyleSheet(""" 
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
    button5.clicked.connect(main_window.danse)

    
    button6 = QPushButton("Wiggle Eyes", main_window)
    button6.setIcon(QtGui.QIcon("images/get_ready"))
    button6.setIconSize(QSize(70, 70))
    button6.setToolTip("Marty Wave-right")
    button6.setStyleSheet(""" 
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
    button6.clicked.connect(lambda: main_window.on_button_click("Wiggle Eyes"))
    
    button7 = QPushButton("Kick right", main_window)
    button7.setIcon(QtGui.QIcon("images/get_ready"))
    button7.setIconSize(QSize(70, 70))
    button7.setToolTip("Marty Wave-right")
    button7.setStyleSheet(""" 
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
    button7.clicked.connect(lambda: main_window.on_button_click("Kick right"))
    
        
    button8 = QPushButton("Kick left", main_window)
    button8.setIcon(QtGui.QIcon("images/get_ready"))
    button8.setIconSize(QSize(70, 70))
    button8.setToolTip("Marty Wave-right")
    button8.setStyleSheet(""" 
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
    button8.clicked.connect(lambda: main_window.on_button_click("Kick left"))

    right_layout_line2 = QHBoxLayout()
    right_layout_line2.addWidget(button5)
    right_layout_line2.addWidget(button6)
    right_layout_line2.addWidget(button7)
    right_layout_line2.addWidget(button8)
    
    container_right_line2 = QWidget()
    container_right_line2.setLayout(right_layout_line2)
    right_layout.addWidget(container_right_line2)
    
    right_layout_line3 = QHBoxLayout()
    slider_label = QLabel("Contrôleur de la vitesse")
    slider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    right_layout_line3.addWidget(slider_label)
    
    
    slider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setTickPosition(QSlider.TickPosition.TicksAbove)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setTickInterval(10)
    slider.setSingleStep(1)
    slider.setValue(50)
        
    def update_speed(value):
        slider_label.setText(f"Vitesse: {value}")

    update_speed = update_speed
    slider.valueChanged.connect(update_speed)
    right_layout.addWidget(slider_label)
    right_layout.addWidget(slider)
    right_layout_line3.addWidget(slider)
    

    slider_label = QLabel("Valeur de la vitesse: 50")
    right_layout_line3.addWidget(slider_label)
    #container_right_line4 = QWidget()
    #container_right_line4.setLayout(right_layout_line3)

    #right_layout_line3.addWidget(button9)
    
    container_right_line3 = QWidget()
    container_right_line3.setLayout(right_layout_line3)
    right_layout.addWidget(container_right_line3)

    return right_layout

    
