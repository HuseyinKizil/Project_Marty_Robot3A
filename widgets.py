from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt, QRect, QTimer
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QSlider, QPushButton
from PyQt6.QtGui import QKeySequence, QShortcut
from layouts_left import create_left_buttons
from layouts_right import create_right_buttons

from martypy import Marty
import tkinter as tk

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.my_marty = Marty("wifi", "192.168.0.107")
        self.setWindowTitle("Marty")
        self.setWindowIcon(QtGui.QIcon("images/home"))
        self.setGeometry(500, 200, 300, 250)
        
        self.detected_colors = []

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
      
        self.reaction()
        
        # Initialize empty list to store detected colors
        self.color_label = QLabel("Couleurs détectées: ")
        right_layout.addWidget(self.color_label)

        # Add button to add color to the list
        self.add_color_button = QPushButton("Ajouter couleur")
        self.add_color_button.clicked.connect(self.add_color)
        right_layout.addWidget(self.add_color_button)
        
        # Add button to display the final list of colors
        self.show_colors_button = QPushButton("Afficher les couleurs détectées")
        self.show_colors_button.clicked.connect(self.show_detected_colors)
        right_layout.addWidget(self.show_colors_button)

    def create_shortcuts(self):
        shortcuts = {
            'Dance': ('7', self.danse),
            'Get ready': ('7', self.get_ready),
            'Show-off': ('7', self.show_off),
            'Up side': ('8', self.avancer),
            'Wave-left': ('9', self.wave_left),
            'Left side': ('4', self.side_left),
            'Stop Marty': ('5', self.stop),
            'Right side': ('e', self.side_right),
            'Down side': ('2', self.reverse),
        }

        for action, (shortcut, func) in shortcuts.items():
            QShortcut(QKeySequence(shortcut), self, func)

    def danse(self):
        print("Marty danse stp")
        self.my_marty.dance()
        
    def get_ready(self):
        self.my_marty.get_ready()
        
    def wave_left(self):     
        self.my_marty.arms(left_angle=250, right_angle=0, move_time=2500)
        
    def wave_right(self):
        self.my_marty.arms(left_angle=0, right_angle=150, move_time=2500)
        
    def side_left(self):
        self.my_marty.sidestep("left", steps=7, step_length=35, move_time=1000, blocking=None)
        
    def side_right(self):
        self.my_marty.sidestep("right", steps=7, step_length=35, move_time=1000, blocking=None)
        
    def avancer(self):
        self.my_marty.walk(num_steps=7, start_foot='auto', turn=0, step_length=25, move_time=1500, blocking=None) 
       
    def reverse(self):
        self.my_marty.walk(num_steps=2, start_foot='auto', turn=0, step_length=-25, move_time=1500, blocking=None) 
        
    def stop(self):
        self.my_marty.stop(stop_type=None)
        
    def celebrate(self):
        self.my_marty.celebrate(move_time=4000, blocking=None) 

    def lire_couleur(self): 
       return self.my_marty.get_ground_sensor_reading("left")
       
    def wiggle(self):
        self.my_marty.eyes(pose="wiggle", move_time=1000, blocking=None)
        
    def kick_right(self):
        self.my_marty.kick(side='right', twist=0, move_time=2500, blocking=None) 
    
    def kick_left(self):
        self.my_marty.kick(side='left', twist=0, move_time=2500, blocking=None) 
        
    def show_off(self):
        self.my_marty.lean(direction="forward", move_time=1 * 1000)

    def update_battery_level(self):
        battery_level = self.my_marty.get_battery_remaining()  # Assuming this method exists
        self.battery_label.setText(f"Niveau de la batterie: {battery_level}%")
        QTimer.singleShot(10000, self.update_battery_level)  # Update every 60 seconds
  
    def color(self):
        cc = self.my_marty.get_ground_sensor_reading("left")
        print(f"Valeur du capteur de couleur gauche : {cc}")  
        
    def reaction(self):
        left_color = self.my_marty.get_ground_sensor_reading("left")
        print(f"Valeur du capteur de couleur gauche : {left_color}")  

        if 70 <= left_color <= 77:
            print("Rouge détecté")
        
        elif 42 <= left_color <= 46:
            print("Bleu détecté")
         
        elif 26 <= left_color <= 30:
            print("Vert détecté")
           
        elif 160 <= left_color <= 164:
            print("Jaune détecté")
  
        elif 83 <= left_color <= 88:
            print("Rose détecté")

        elif 18 <= left_color <= 22:
            print("Bleu foncé détecté")

        elif 12 <= left_color <= 16:
            print("Noir détecté")
        
        else:
            print("Couleur non reconnue")
            
    def get_color_sensor(self, left):
        return self.my_marty.get_ground_sensor_reading(left)

    def add_color(self):
        color_value = self.lire_couleur()
        self.detected_colors.append(color_value)
        self.color_label.setText(f"Couleurs détectées: {self.detected_colors}")

    def show_detected_colors(self):
        print("Couleurs détectées:", self.detected_colors)
        self.color_label.setText(f"Couleurs détectées: {self.detected_colors}")

