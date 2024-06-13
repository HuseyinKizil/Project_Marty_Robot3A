import marty_the_robot
from marty_the_robot import Marty
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

# Connexion à Marty
marty = Marty('wifi', ip='adresse_ip_de_marty')

# Dictionnaire de correspondance des valeurs hexadécimales aux noms de couleurs
hex_to_color = {
    '#FF0000': 'Rouge',
    '#00FF00': 'Vert',
    '#0000FF': 'Bleu',
    '#FFFF00': 'Jaune',
    '#FFFFFF': 'Blanc',
    # Ajouter d'autres correspondances si nécessaire
}

# Fonction pour convertir une valeur hexadécimale en nom de couleur
def hex_to_color_name(hex_value):
    return hex_to_color.get(hex_value, "Inconnue")

class ColorSensorApp(QWidget):
    def __init__(self, my_marty):
        super().__init__()
        self.my_marty = my_marty
        self.color_label = QLabel("Couleur détectée: Inconnue", self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.color_label)
        self.setLayout(layout)
        
        self.lire_couleur()
    
    def lire_couleur(self):
        color_hex = self.my_marty.get_color_sensor_hex("LeftColorSensor")
        color_name = hex_to_color_name(color_hex)
        self.color_label.setText(f"Couleur détectée: {color_name}")
        QTimer.singleShot(10000, self.lire_couleur)  # Mise à jour toutes les 10 secondes

# Initialisation de l'application PyQt
app = QApplication(sys.argv)
my_marty = Marty('wifi', ip='adresse_ip_de_marty')
window = ColorSensorApp(my_marty)
window.show()
sys.exit(app.exec_())
