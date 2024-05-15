import sys

from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt,QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget,QHBoxLayout,QPushButton,QToolBar,QStatusBar,QSlider
from PyQt6.QtGui import QAction,QIcon
from PyQt6 import QtCore
from typing import Optional
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
   def __init__(self):
        super().__init__()
        
        left = 500
        top = 200
        width = 300
        height = 250

        self.setWindowTitle("Marty")
        self.setWindowIcon(QtGui.QIcon("home"))
        self.setGeometry(left,top,width,height)

 
        #def dance(self,side: str = 'right', move_time: int = 3000, blocking: Optional[bool] = None) -> bool:

        #def wiggle(self,move_time: int = 4000, blocking: Optional[bool] = None) -> bool:

        # Connectez les boutons à leurs fonctions respectives
        #button1_line2_right.clicked.connect(self.dance)
    
       
        main_layout= QHBoxLayout()

        left_layout= QVBoxLayout()

        left_layout_line1= QHBoxLayout()
       
        button1_line1_left= QPushButton("",self)
        button1_line1_left.setGeometry(QRect(300,300,211,23))
        button1_line1_left.setIcon(QtGui.QIcon("pivot_gauche"))
        button1_line1_left.setIconSize(QtCore.QSize(40,40))
        button1_line1_left.setToolTip("This is Click Me")
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
        button2_line1_left.setGeometry(QRect(300,300,211,23))
        button2_line1_left.setIcon(QtGui.QIcon("haut"))
        button2_line1_left.setIconSize(QtCore.QSize(40,40))
        button2_line1_left.setToolTip("This is Click Me")
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
        button3_line1_left.setGeometry(QRect(300,300,211,23))
        button3_line1_left.setIcon(QtGui.QIcon("pivot_droit"))
        button3_line1_left.setIconSize(QtCore.QSize(40,40))
        button3_line1_left.setToolTip("This is Click Me")
        button3_line1_left.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
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
        button1_line2_left.setGeometry(QRect(300,300,211,23))
        button1_line2_left.setIcon(QtGui.QIcon("gauche"))
        button1_line2_left.setIconSize(QtCore.QSize(40,40))
        button1_line2_left.setToolTip("This is Click Me")
        button1_line2_left.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            color: "";
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: "white";
        }
                              
        """)
        
        button2_line2_left= QPushButton("",self)
        button2_line2_left.setGeometry(QRect(300,300,211,23))
        button2_line2_left.setIcon(QtGui.QIcon("centre"))
        button2_line2_left.setIconSize(QtCore.QSize(40,40))
        button2_line2_left.setToolTip("This is Click Me")
        button2_line2_left.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
            color: "";
        } 
        QPushButton:hover {
            font-size:18px;
            background-color:"#00FFFF";
            color: "white";
        }
                              
        """)
        button3_line2_left= QPushButton("",self)
        button3_line2_left.setGeometry(QRect(300,300,211,23))
        button3_line2_left.setIcon(QtGui.QIcon("droite"))
        button3_line2_left.setIconSize(QtCore.QSize(40,40))
        button3_line2_left.setToolTip("This is Click Me")
        button3_line2_left.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
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
        button2_line3_left.setGeometry(QRect(300,300,211,23))
        button2_line3_left.setIcon(QtGui.QIcon("bas"))
        button2_line3_left.setIconSize(QtCore.QSize(40,40))
        button2_line3_left.setToolTip("This is Click Me")
        button2_line3_left.setStyleSheet(""" 
        QPushButton {
            font-size:16px;
            background-color:"#87CEEB";
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
        button1_line1_right.setIcon(QtGui.QIcon("get_ready"))
        button1_line1_right.setIconSize(QtCore.QSize(70,70))
        button1_line1_right.setToolTip("Marty is ready")
        button1_line1_right.setStyleSheet(""" 
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

        button2_line1_right= QPushButton("Show-off",self)
        button2_line1_right.setGeometry(QRect(300,300,211,23))
        button2_line1_right.setIcon(QtGui.QIcon("get_ready"))
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
        button3_line1_right.setGeometry(QRect(300,300,211,23))
        button3_line1_right.setIcon(QtGui.QIcon("get_ready"))
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
        button4_line1_right.setGeometry(QRect(300,300,211,23))
        button4_line1_right.setIcon(QtGui.QIcon("get_ready"))
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
        button1_line2_right.setGeometry(QRect(300,300,211,23))
        button1_line2_right.setIcon(QtGui.QIcon("dance"))
        button1_line2_right.setIconSize(QtCore.QSize(70,70))
        button1_line2_right.setToolTip("Marty dances")
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
        button2_line2_right.setGeometry(QRect(300,300,211,23))
        button2_line2_right.setIcon(QtGui.QIcon("wiggle"))
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
        button3_line2_right.setGeometry(QRect(500,500,300,100))
        button3_line2_right.setIcon(QtGui.QIcon("kick_left"))
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
        button4_line2_right.setGeometry(QRect(300,300,211,23))
        button4_line2_right.setIcon(QtGui.QIcon("get_ready"))
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
        
        right_layout_line2.addWidget(button1_line2_right)
        right_layout_line2.addWidget(button2_line2_right)
        right_layout_line2.addWidget(button3_line2_right)
        right_layout_line2.addWidget(button4_line2_right)
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
