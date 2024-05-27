from PyQt6 import QtGui
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QSlider
from PyQt6.QtGui import QKeySequence, QShortcut
from layouts import create_left_buttons, create_right_buttons

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