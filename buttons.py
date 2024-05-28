from PyQt6.QtCore import QSize, Qt, QRect
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

    right_layout_line1 = QHBoxLayout()

    button1_line1_right = QPushButton("Get ready", main_window)
    button1_line1_right.setGeometry(QRect(300, 300, 211, 23))
    button1_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
    button1_line1_right.setIconSize(QSize(70, 70))
    button1_line1_right.setToolTip("Marty is ready")
    button1_line1_right.setStyleSheet(""" 
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
    button1_line1_right.clicked.connect(lambda: main_window.on_button_click("Get ready"))

    button2_line1_right = QPushButton("Show-off", main_window)
    button2_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
    button2_line1_right.setIconSize(QSize(70, 70))
    button2_line1_right.setToolTip("Marty shows-off")
    button2_line1_right.setStyleSheet(""" 
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
    button2_line1_right.clicked.connect(lambda: main_window.on_button_click("Show-off"))

    button3_line1_right = QPushButton("Wave-left", main_window)
    button3_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
    button3_line1_right.setIconSize(QSize(70, 70))
    button3_line1_right.setToolTip("Marty Wave-left")
    button3_line1_right.setStyleSheet(""" 
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
    button3_line1_right.clicked.connect(lambda: main_window.on_button_click("Wave-left"))

    button4_line1_right = QPushButton("Wave-right", main_window)
    button4_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
    button4_line1_right.setIconSize(QSize(70, 70))
    button4_line1_right.setToolTip("Marty waves-right")
    button4_line1_right.setStyleSheet(""" 
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
    button4_line1_right.clicked.connect(lambda: main_window.on_button_click("Wave-right"))

    right_layout_line1.addWidget(button1_line1_right)
    right_layout_line1.addWidget(button2_line1_right)
    right_layout_line1.addWidget(button3_line1_right)
    right_layout_line1.addWidget(button4_line1_right)
    container_right_line1 = QWidget()
    container_right_line1.setLayout(right_layout_line1)
    right_layout.addWidget(container_right_line1)

    right_layout_line2 = QHBoxLayout()

    button1_line2_right = QPushButton("Dance!", main_window)
    button1_line2_right.setIcon(QtGui.QIcon("images/dance"))
    button1_line2_right.setIconSize(QSize(70, 70))
    button1_line2_right.setToolTip("Marty's dance")
    button1_line2_right.setStyleSheet(""" 
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
    button1_line2_right.clicked.connect(lambda: main_window.on_button_click("Dance!"))

    button2_line2_right = QPushButton("Wiggle Eyes", main_window)
    button2_line2_right.setIcon(QtGui.QIcon("images/wiggle"))
    button2_line2_right.setIconSize(QSize(70, 70))
    button2_line2_right.setToolTip("Marty wiggle eyes")
    button2_line2_right.setStyleSheet(""" 
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
    button2_line2_right.clicked.connect(lambda: main_window.on_button_click("Wiggle Eyes"))

    button3_line2_right = QPushButton("Kick left", main_window)
    button3_line2_right.setIcon(QtGui.QIcon("images/kick_left"))
    button3_line2_right.setIconSize(QSize(70, 70))
    button3_line2_right.setToolTip("Marty kicks left")
    button3_line2_right.setStyleSheet(""" 
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
    button3_line2_right.clicked.connect(lambda: main_window.on_button_click("Kick left"))

    button4_line2_right = QPushButton("Kick right", main_window)
    button4_line2_right.setIcon(QtGui.QIcon("images/get_ready"))
    button4_line2_right.setIconSize(QSize(70, 70))
    button4_line2_right.setToolTip("Marty kicks right")
    button4_line2_right.setStyleSheet(""" 
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
    button4_line2_right.clicked.connect(lambda: main_window.on_button_click("Kick right"))

    right_layout_line2.addWidget(button1_line2_right)
    right_layout_line2.addWidget(button2_line2_right)
    right_layout_line2.addWidget(button3_line2_right)
    right_layout_line2.addWidget(button4_line2_right)

    container_right_line2 = QWidget()
    container_right_line2.setLayout(right_layout_line2)
    right_layout.addWidget(container_right_line2)
    right_layout_line3 = QHBoxLayout()

    slider_label = QLabel("Contrôleur de la vitesse")
    slider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    right_layout_line3.addWidget(slider_label)

    main_window.slider = QSlider(Qt.Orientation.Horizontal)
    main_window.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
    main_window.slider.setMinimum(0)
    main_window.slider.setMaximum(100)
    main_window.slider.setTickInterval(10)
    main_window.slider.setSingleStep(1)
    main_window.slider.setValue(50)
        
    def update_speed(value):
        main_window.slider_label.setText(f"Vitesse: {value}")

    main_window.update_speed = update_speed
    main_window.slider.valueChanged.connect(main_window.update_speed)
    right_layout.addWidget(slider_label)
    right_layout.addWidget(main_window.slider)
    right_layout_line3.addWidget(main_window.slider)

    container_right_line3 = QWidget()
    container_right_line3.setLayout(right_layout_line3)
    right_layout.addWidget(container_right_line3)

    right_layout_line4 = QHBoxLayout()

    main_window.slider_label = QLabel("Valeur de la vitesse: 50")
    right_layout_line4.addWidget(main_window.slider_label)
    container_right_line4 = QWidget()
    container_right_line4.setLayout(right_layout_line4)
    right_layout.addWidget(container_right_line4)

    container_right = QWidget()
    container_right.setLayout(right_layout)

    right_layout.addWidget(container_right)
    container = QWidget()
    container.setLayout(right_layout)
    # Set the central widget of the Window.
    main_window.setCentralWidget(container)


    return right_layout
