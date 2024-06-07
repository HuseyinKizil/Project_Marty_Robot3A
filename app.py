import sys
from martypy import Marty
from PyQt6 import QtGui,QtCore
from PyQt6.QtCore import QSize, Qt,QRect,QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget,QHBoxLayout,QPushButton,QToolBar,QStatusBar,QSlider
from PyQt6.QtGui import QAction,QIcon,QKeyEvent
from typing import Optional
from widgets import MainWindow


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
   def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Marty")
        self.setWindowIcon(QtGui.QIcon("images/home"))
        self.setGeometry(500,200,300,250)
        self.setStyleSheet("background-color:#DFF2FF")
        
        main_layout= QHBoxLayout()

        left_layout= QVBoxLayout()

        left_layout_line1= QHBoxLayout()
       
        button1_line1_left= QPushButton("",self)
        button1_line1_left.setIcon(QtGui.QIcon("images/pivot_gauche"))
        button1_line1_left.setIconSize(QSize(40,40))
        button1_line1_left.setToolTip("left side rotation")
        button1_line1_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid yellow; 
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }
                              
        """)
       
        button2_line1_left= QPushButton("",self)
        button2_line1_left.setIcon(QtGui.QIcon("images/haut"))
        button2_line1_left.setIconSize(QtCore.QSize(40,40))
        button2_line1_left.setToolTip("up side")
        button2_line1_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid blue; 
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
        }      
        """)
        button3_line1_left= QPushButton("",self)
        button3_line1_left.setIcon(QtGui.QIcon("images/pivot_droit"))
        button3_line1_left.setIconSize(QtCore.QSize(40,40))
        button3_line1_left.setToolTip("right side rotation")
        button3_line1_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid pink; 
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }
                              
        """)


        left_layout_line1.addWidget(button1_line1_left)
        left_layout_line1.addWidget(button2_line1_left)
        left_layout_line1.addWidget(button3_line1_left)
        container_left_line1=QWidget()
        container_left_line1.setLayout(left_layout_line1)
        left_layout.addWidget(container_left_line1)

        
        left_layout_line2= QHBoxLayout()

        button1_line2_left= QPushButton("",self)
        button1_line2_left.setIcon(QtGui.QIcon("images/gauche"))
        button1_line2_left.setIconSize(QtCore.QSize(40,40))
        button1_line2_left.setToolTip("Left side")
        button1_line2_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid purple; 
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }
                              
        """)
        
        button2_line2_left= QPushButton("",self)
        button2_line2_left.setIcon(QtGui.QIcon("images/centre"))
        button2_line2_left.setIconSize(QtCore.QSize(40,40))
        button2_line2_left.setToolTip("Stop Marty")
        button2_line2_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid white; 
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }
                              
        """)
        button3_line2_left= QPushButton("",self)
        button3_line2_left.setIcon(QtGui.QIcon("images/droite"))
        button3_line2_left.setIconSize(QtCore.QSize(40,40))
        button3_line2_left.setToolTip("This is Click Me")
        button3_line2_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid green; 
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }
                              
        """)    
        left_layout_line2.addWidget(button1_line2_left)
        left_layout_line2.addWidget(button2_line2_left)
        left_layout_line2.addWidget(button3_line2_left)
        container_left_line2=QWidget()
        container_left_line2.setLayout(left_layout_line2)
        left_layout.addWidget(container_left_line2)

         
        left_layout_line3= QHBoxLayout()

        button2_line3_left= QPushButton("",self)
        button2_line3_left.setIcon(QtGui.QIcon("images/bas"))
        button2_line3_left.setIconSize(QtCore.QSize(40,40))
        button2_line3_left.setToolTip("This is Click Me")
        button2_line3_left.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid orange; 
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }          
        """)
        button1_line3_left= QLabel("")
        button3_line3_left= QLabel("",self)
        left_layout_line3.addWidget(button1_line3_left)
        left_layout_line3.addWidget(button2_line3_left)
        left_layout_line3.addWidget(button3_line3_left)
        container_left_line3=QWidget()
        container_left_line3.setLayout(left_layout_line3)
        left_layout.addWidget(container_left_line3)


        container_left = QWidget()
        container_left.setLayout(left_layout)

        right_layout= QVBoxLayout()

        right_layout_line1= QHBoxLayout()
        
        button1_line1_right= QPushButton("Get ready",self)
        button1_line1_right.setGeometry(QRect(300,300,211,23))
        button1_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
        button1_line1_right.setIconSize(QtCore.QSize(70,70))
        button1_line1_right.setToolTip("Marty is ready")
        button1_line1_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black;
                border-radius: 10px;
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            } 
                              
        """)

        button2_line1_right= QPushButton("Show-off",self)
        button2_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
        button2_line1_right.setIconSize(QtCore.QSize(70,70))
        button2_line1_right.setToolTip("Marty shows-off")
        button2_line1_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black; border-radius: 10px;
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            } 
                              
        """)
        button3_line1_right= QPushButton("Wave-left",self)
        button3_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
        button3_line1_right.setIconSize(QtCore.QSize(70,70))
        button3_line1_right.setToolTip("Marty Wave-left")
        button3_line1_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black; border-radius: 10px;
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }                              
        """)
        button4_line1_right= QPushButton("Show-off",self)
        button4_line1_right.setIcon(QtGui.QIcon("images/get_ready"))
        button4_line1_right.setIconSize(QtCore.QSize(70,70))
        button4_line1_right.setToolTip("Marty waves-right")
        button4_line1_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black; border-radius: 10px;
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            } 
                              
        """)

        right_layout_line1.addWidget(button1_line1_right)
        right_layout_line1.addWidget(button2_line1_right)
        right_layout_line1.addWidget(button3_line1_right)
        right_layout_line1.addWidget(button4_line1_right)
        container_right_line1=QWidget()
        container_right_line1.setLayout(right_layout_line1)
        right_layout.addWidget(container_right_line1)

        right_layout_line2= QHBoxLayout()

        button1_line2_right= QPushButton("Dance!",self)
        button1_line2_right.setIcon(QtGui.QIcon("images/dance"))
        button1_line2_right.setIconSize(QtCore.QSize(70,70))
        button1_line2_right.setToolTip("Marty's dance")
        button1_line2_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black; border-radius: 10px;
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            } 
                              
        """)

        button2_line2_right= QPushButton("Wiggle Eyes",self)
        button2_line2_right.setIcon(QtGui.QIcon("images/wiggle"))
        button2_line2_right.setIconSize(QtCore.QSize(70,70))
        button2_line2_right.setToolTip("Marty wiggle eyes")
        button2_line2_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black; border-radius: 10px;
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            }                              
        """)
        button3_line2_right= QPushButton("Kick left",self)
        button3_line2_right.setIcon(QtGui.QIcon("images/kick_left"))
        button3_line2_right.setIconSize(QtCore.QSize(70,70))
        button3_line2_right.setToolTip("Marty kicks left")
        button3_line2_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                border: 1px solid black; border-radius: 10px;
                background-color:"#87CEEB";
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            } 
                              
        """)
        button4_line2_right= QPushButton("Kick right",self)
        button4_line2_right.setIcon(QtGui.QIcon("images/get_ready"))
        button4_line2_right.setIconSize(QtCore.QSize(70,70))
        button4_line2_right.setToolTip("Marty kick right")
        button4_line2_right.setStyleSheet(""" 
            QPushButton {
                font-size:16px;
                background-color:"#87CEEB";
                border: 1px solid black; border-radius: 10px;                              
                color: "";
            } 
            QPushButton:hover {
                font-size:18px;
                background-color:"#00FFFF";
                color: "white";
            } 
                              
        """)
        #Définition des fonctions
        def on_button_click(self):
        # Méthode appelée lorsque le bouton est cliqué
            print("Le bouton a été cliqué!")
      
        self.on_button_click = on_button_click
      
        button4_line2_right.clicked.connect(self.on_button_click)
   
        right_layout_line2.addWidget(button1_line2_right)
        right_layout_line2.addWidget(button2_line2_right)
        right_layout_line2.addWidget(button3_line2_right)
        right_layout_line2.addWidget(button4_line2_right)

        container_right_line2=QWidget()
        container_right_line2.setLayout(right_layout_line2)
        right_layout.addWidget(container_right_line2)

        right_layout_line3 = QHBoxLayout()

        slider_label = QLabel("Contrôleur de la vitesse")
        slider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout_line3.addWidget(slider_label)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)
        self.slider.setValue(50)
        
        def update_speed(value):
            self.slider_label.setText(f"Vitesse: {value}")

        self.update_speed = update_speed
        self.slider.valueChanged.connect(self.update_speed)
        right_layout.addWidget(slider_label)
        right_layout.addWidget(self.slider)
        right_layout_line3.addWidget(self.slider)

        container_right_line3 = QWidget()
        container_right_line3.setLayout(right_layout_line3)
        right_layout.addWidget(container_right_line3)

        right_layout_line4 = QHBoxLayout()

        self.slider_label = QLabel("Valeur de la vitesse: 50")
        right_layout_line4.addWidget(self.slider_label)
        
        container_right_line4 = QWidget()
        container_right_line4.setLayout(right_layout_line4)
        right_layout.addWidget(container_right_line4)
            
        
        container_right = QWidget()
        container_right.setLayout(right_layout)

        main_layout.addWidget(container_left)
        main_layout.addWidget(container_right)
        container = QWidget()
        container.setLayout(main_layout)
        # Set the central widget of the Window.
        self.setCentralWidget(container)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


