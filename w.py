from martypy import Marty
import logging

# Configurer le niveau de journalisation pour obtenir plus de détails
logging.basicConfig(level=logging.DEBUG)

# Remplacez par l'adresse IP correcte de votre Marty
marty_ip = "192.168.0.3"

try:
    marty = Marty('wifi', marty_ip)
    marty.hello()
except Exception as e:
    print(f"Error connecting to Marty: {e}")

