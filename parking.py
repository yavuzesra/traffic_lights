import time
from grovepi import *
from grove_rgb_lcd import *

# Configuration des ports
sensor_entrance = 7  # Capteur à l'entrée connecté au port D7
sensor_exit = 8      # Capteur à la sortie connecté au port D8
lcd = 4              # Écran LCD RGB connecté à un port I2C

# Initialisation
pinMode(sensor_entrance, "INPUT")
pinMode(sensor_exit, "INPUT")
setRGB(0, 128, 64)  # Couleur de fond de l'écran LCD

# Nombre initial de places disponibles
places_disponibles = 10

try:
    while True:
        # Détecter l'entrée d'une voiture
        if digitalRead(sensor_entrance) == 1:
            if places_disponibles > 0:
                places_disponibles -= 1
                time.sleep(1)  # Délai pour éviter la double détection

        # Détecter la sortie d'une voiture
        elif digitalRead(sensor_exit) == 1:
            if places_disponibles < 10:
                places_disponibles += 1
                time.sleep(1)  # Délai pour éviter la double détection

        # Afficher le nombre de places disponibles
        setText_norefresh("Places disponibles: " + str(places_disponibles))
        time.sleep(0.5)  # Mise à jour toutes les 0.5 secondes

except KeyboardInterrupt:
    setText("")
    setRGB(0,0,0)  # Éteindre l'écran LCD
    print("Programme terminé.")
