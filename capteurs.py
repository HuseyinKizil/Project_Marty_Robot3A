import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider, QLabel, QHBoxLayout
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, QTimer
import cv2
import serial
import numpy as np
from pyzbar.pyzbar import decode


# Communication série avec le robot (ajustez le port et le baudrate selon votre configuration)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # à adapter

# Ajouter un label pour afficher les données des capteurs
        self.sensor_label = QLabel("Sensor Data: ")

    layout.addWidget(self.sensor_label)

# Ajouter une zone pour afficher le flux vidéo
        self.video_label = QLabel()
        layout.addWidget(self.video_label)

# Démarrer un timer pour lire les données des capteurs périodiquement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_sensor_data)
        self.timer.start(1000)  # Lire les données chaque seconde

  # Initialiser la capture vidéo
        self.cap = cv2.VideoCapture(0)
        self.video_timer = QTimer(self)
        self.video_timer.timeout.connect(self.update_video)
        self.video_timer.start(30)  # Mettre à jour la vidéo toutes les 30 ms

 def send_command(self, command):
        self.ser.write(command.encode())

    def read_sensor_data(self):
        # Lire les données des capteurs depuis le port série
        if self.ser.in_waiting > 0:
            sensor_data = self.ser.readline().decode().strip()
            self.sensor_label.setText(f"Sensor Data: {sensor_data}")
            print(f"Sensor Data: {sensor_data}")

    def update_video(self):
        ret, frame = self.cap.read()

         if ret:
            # Convertir l'image pour l'affichage dans PyQt
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(qt_image))

            # Analyse de l'image pour détecter les QR codes
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    points = hull
                n = len(points)
                for j in range(0, n):
                    cv2.line(frame, tuple(points[j]), tuple(points[(j + 1) % n]), (255, 0, 0), 3)
                x = obj.rect.left
                y = obj.rect.top
                cv2.putText(frame, obj.data.decode('utf-8'), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
