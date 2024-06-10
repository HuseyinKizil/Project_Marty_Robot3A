from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt, QRect,QTimer
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QSlider, QPushButton
from PyQt6.QtGui import QKeySequence, QShortcut
from layouts import create_left_buttons
from layouts_right import create_right_buttons
from martypy import Marty

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Marty")
        self.setWindowIcon(QtGui.QIcon("images/home"))
        self.setGeometry(500, 200, 300, 250)

        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        left_layout = create_left_buttons(self)
        right_layout = create_right_buttons(self)

        container_left = QWidget()
        container_left.setLayout(left_layout)

        container_right = QWidget()
        container_right.setLayout(right_layout)

        main_layout.addWidget(container_left)
        main_layout.addWidget(container_right)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        # Adding keyboard shortcuts
        self.create_shortcuts()

        # Adding battery level display
        self.battery_label = QLabel("Niveau de la batterie: ")
        right_layout.addWidget(self.battery_label)
        self.update_battery_level()

         # Initialize empty list to store detected colors
        self.detected_colors = []
        self.color_label = QLabel("Couleurs détectées: Aucun")
        right_layout.addWidget(self.color_label)

        # Adding a button for detecting colors
        self.detect_color_button = QPushButton("Détecter la couleur", self)
        self.detect_color_button.clicked.connect(self.update_detected_colors)
        right_layout.addWidget(self.detect_color_button)

    def create_shortcuts(self):
        shortcuts = {
            'left side rotation': ('7', lambda: self.on_button_click("left side rotation")),
            'up side': ('8', lambda: self.on_button_click("up side")),
            'right side rotation': ('9', lambda: self.on_button_click("right side rotation")),
            'Left side': ('4', lambda: self.on_button_click("Left side")),
            'Stop Marty': ('5', lambda: self.on_button_click("Stop Marty")),
            'Right side': ('6', lambda: self.on_button_click("Right side")),
            'Down side': ('2', lambda: self.on_button_click("Down side")),
        }

        for action, (shortcut, func) in shortcuts.items():
            QShortcut(QKeySequence(shortcut), self, func)
        
    def on_button_click(self, message):
        print(f"Button clicked: {message}")
        
    def danse(self):
        print("Marty danse stp")
        self.my_marty.dance()
        
    def get_ready(self):
        self.my_marty.get_ready()
        
    def wave_left(self):     
        self.my_marty.arms(left_angle=250, right_angle=0,move_time=2500)
        
    def wave_right(self):
        self.my_marty.arms(left_angle=0, right_angle=150,move_time=2500)
        
    def side_left(self):
        self.my_marty.sidestep("left", steps = 1, step_length=35, move_time = 1000, blocking = None)
        
    def side_right(self):
       self.my_marty.sidestep("right", steps = 1, step_length=35, move_time = 1000, blocking = None)
        
        
    def avancer(self):
        self.my_marty.walk(num_steps= 5, start_foot ='auto', turn = 0, step_length = 25, move_time = 1500, blocking = None) 
       
         
    def reverse(self):
        self.my_marty.walk(num_steps=2, start_foot ='auto', turn = 0, step_length =-25, move_time = 1500, blocking = None) 
        
    def stop(self):
        self.my_marty.stop(stop_type=None)
        
    def celebrate(self):
        self.my_marty.celebrate(move_time = 4000, blocking = None) 

    def color(self): 
       self. my_marty.get_color_sensor_color("Select")
       
    def wiggle(self):
        self.my_marty.eyes(pose="wiggle", move_time = 1000, blocking = None)
        
    def kick_right(self):
        self.my_marty.kick(side= 'right', twist= 0, move_time = 2500, blocking = None) 
    
    def kick_left(self):
        self.my_marty.kick(side= 'left', twist= 0, move_time = 2500, blocking = None) 
        
    def show_off(self):
        self.my_marty.lean(direction="forward", move_time=1 * 1000)