import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

class RobotController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Controller")

        # Créez les boutons pour piloter le robot
        self.forward_button = QPushButton("Forward")
        self.backward_button = QPushButton("Backward")
        self.left_button = QPushButton("Left")
        self.right_button = QPushButton("Right")
        self.stop_button = QPushButton("Stop")

        # Connectez les boutons à leurs fonctions respectives
        self.forward_button.clicked.connect(self.move_forward)
        self.backward_button.clicked.connect(self.move_backward)
        self.left_button.clicked.connect(self.move_left)
        self.right_button.clicked.connect(self.move_right)
        self.stop_button.clicked.connect(self.stop_robot)

        # Créez un slider pour contrôler la vitesse du robot
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(100)
        self.speed_slider.setValue(50)  # Valeur par défaut
        self.speed_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.speed_slider.setTickInterval(10)
        
        # Créez un label pour afficher la valeur de la vitesse
        self.speed_label = QLabel(f"Speed: {self.speed_slider.value()}")

        # Connectez le slider à la méthode de mise à jour de la vitesse
        self.speed_slider.valueChanged.connect(self.update_speed)

        # Position des boutons et du slider
        layout = QVBoxLayout()
        layout.addWidget(self.forward_button)
        layout.addWidget(self.backward_button)
        layout.addWidget(self.left_button)
        layout.addWidget(self.right_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.speed_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initialiser la vitesse
        self.speed = self.speed_slider.value()

    def update_speed(self):
        self.speed = self.speed_slider.value()
        self.speed_label.setText(f"Speed: {self.speed}")
        print(f"Speed set to {self.speed}")
        # Code pour envoyer la nouvelle vitesse au robot, si nécessaire

    def move_forward(self):
        print(f"Moving forward at speed {self.speed}")
        # Code pour envoyer la commande de déplacement avant au robot

    def move_backward(self):
        print(f"Moving backward at speed {self.speed}")
        # Code pour envoyer la commande de déplacement arrière au robot

    def move_left(self):
        print(f"Turning left at speed {self.speed}")
        # Code pour envoyer la commande de tourner à gauche au robot

    def move_right(self):
        print(f"Turning right at speed {self.speed}")
        # Code pour envoyer la commande de tourner à droite au robot

    def stop_robot(self):
        print("Stopping robot")
        # Code pour envoyer la commande d'arrêt au robot

    def keyPressEvent(self, event: QKeyEvent):
        # touches clavier
        if event.key() == Qt.Key_Z:
            self.move_forward()
        elif event.key() == Qt.Key_S:
            self.move_backward()
        elif event.key() == Qt.Key_Q:
            self.move_left()
        elif event.key() == Qt.Key_D:
            self.move_right()
        elif event.key() == Qt.Key_Space:
            self.stop_robot()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobotController()
    window.show()
    sys.exit(app.exec())
