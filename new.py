import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QColor

class MainWindow(QWidget):
    def _init_(self):
        super()._init_()

        self.setWindowTitle("Interface principale")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Création du bouton "Commencer"
        btn_commencer = QPushButton("Commencer", self)
        btn_commencer.setStyleSheet("background-color: red;") # Définition de la couleur de fond
        btn_commencer.clicked.connect(self.ouvrir_autre_interface) # Lier le clic à la fonction ouvrir_autre_interface
        layout.addWidget(btn_commencer)

        # Création du bouton "Quitter"
        btn_quitter = QPushButton("Quitter", self)
        btn_quitter.setStyleSheet("background-color: green;") # Définition de la couleur de fond
        btn_quitter.clicked.connect(self.close) # Lier le clic à la fonction close (pour fermer l'application)
        layout.addWidget(btn_quitter)

        self.setLayout(layout)

    def ouvrir_autre_interface(self):
        # Fermer l'interface principale
        self.close()

        # Ouvrir une autre interface (à remplacer par votre propre code)
        # Par exemple :
        # autre_interface = AutreInterface()
        # autre_interface.show()
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()