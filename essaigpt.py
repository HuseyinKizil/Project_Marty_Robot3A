import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QVBoxLayout, QWidget
from martypy import Marty

class RobotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.marty1 = Marty('robot1_ip')  # Remplacez 'robot1_ip' par l'adresse IP du robot
        self.marty2 = Marty('robot2_ip')  # Remplacez 'robot2_ip' par l'adresse IP du robot

        # Mettre à jour l'état de la batterie au démarrage
        self.update_battery_status()

        # Mettre à jour l'état de la batterie toutes les 10 secondes
        self.battery_timer = QTimer(self)
        self.battery_timer.timeout.connect(self.update_battery_status)
        self.battery_timer.start(10000)  # 10 secondes

    def initUI(self):
        self.setWindowTitle('Robot App')
        
        # Widgets de l'interface
        self.startDiscoveryButton = QPushButton('Démarrer Découverte', self)
        self.startDiscoveryButton.clicked.connect(self.start_discovery)

        self.concatButton = QPushButton('Concaténer Parcours', self)
        self.concatButton.clicked.connect(self.concat_parcours)
        self.concatButton.setEnabled(False)  # Désactivé jusqu'à la fin de la découverte

        self.startFinalButton = QPushButton('Démarrer Parcours Final', self)
        self.startFinalButton.clicked.connect(self.start_final_parcours)
        self.startFinalButton.setEnabled(False)  # Désactivé jusqu'à la concaténation

        self.parcoursText = QTextEdit(self)
        self.parcoursText.setReadOnly(True)

        self.batteryLabel1 = QLabel('Batterie Robot 1: Inconnu', self)
        self.batteryLabel2 = QLabel('Batterie Robot 2: Inconnu', self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.startDiscoveryButton)
        layout.addWidget(self.concatButton)
        layout.addWidget(self.startFinalButton)
        layout.addWidget(self.batteryLabel1)
        layout.addWidget(self.batteryLabel2)
        layout.addWidget(self.parcoursText)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_battery_status(self):
        try:
            battery1 = self.marty1.get_battery_remaining()
            self.batteryLabel1.setText(f'Batterie Robot 1: {battery1:.2f}%')
        except Exception as e:
            self.batteryLabel1.setText('Batterie Robot 1: Erreur')

        try:
            battery2 = self.marty2.get_battery_remaining()
            self.batteryLabel2.setText(f'Batterie Robot 2: {battery2:.2f}%')
        except Exception as e:
            self.batteryLabel2.setText('Batterie Robot 2: Erreur')

    def start_discovery(self):
        # Grilles initialement vides (les robots découvriront les couleurs)
        self.grille1 = [[None for _ in range(3)] for _ in range(3)]
        self.grille2 = [[None for _ in range(3)] for _ in range(3)]

        # Découverte des grilles par les robots
        self.parcours1 = self.discover_parcours(self.grille1, self.marty1)
        self.parcours2 = self.discover_parcours(self.grille2, self.marty2)

        # Activer le bouton de concaténation après la découverte
        self.concatButton.setEnabled(True)

        self.parcoursText.append("Découverte terminée.\n")

    def discover_parcours(self, grille, marty):
        parcours = []
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                # Simuler la découverte de la couleur par le robot (remplacer par le code réel)
                couleur_detectee = self.simulate_color_detection(i, j)
                grille[i][j] = couleur_detectee
                parcours.append(couleur_detectee)
                # marty.move(...)  # Exemple de commande de déplacement
                # couleur_detectee = marty.read_color_sensor()  # Exemple de lecture de capteur
        return parcours

    def simulate_color_detection(self, i, j):
        # Simuler la détection des couleurs (pour l'exemple, retournez une couleur aléatoire)
        couleurs = ['Rouge', 'Vert', 'Bleu', 'Jaune']
        from random import choice
        return choice(couleurs)

    def concat_parcours(self):
        # Combiner les parcours des deux robots
        self.parcours_final = self.parcours1 + self.parcours2
        self.parcoursText.append("Parcours final combiné: " + str(self.parcours_final))

        # Activer le bouton de parcours final après la concaténation
        self.startFinalButton.setEnabled(True)

    def start_final_parcours(self):
        # Exécuter le parcours final combiné par les robots
        self.execute_final_parcours(self.parcours_final)

    def execute_final_parcours(self, parcours):
        self.parcoursText.append("Exécution du parcours final: " + str(parcours))
        for couleur in parcours:
            # Simuler l'exécution du parcours par les robots (remplacer par le code réel)
            self.parcoursText.append(f"Déplacement vers {couleur}")
            # marty.move(...)  # Exemple de commande de déplacement

def main():
    app = QApplication(sys.argv)
    ex = RobotApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
