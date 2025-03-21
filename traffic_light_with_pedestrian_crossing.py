import grovepi  
import time
from gpiozero import LED
# Configuration des ports
red_led = LED(17)  # Premier feu rouge (pour voitures)
red_led_2 = LED(22) # Second feu rouge (pour piéton)
green_led = LED(18)  # Premier feu vert (pour voiture)
green_led_2 = LED(23)  # Second feu vert (pour piéton)
button = 2  # Bouton connecté au port D2

magnetic_sensor = 3  # Capteur magnétique connecté au port D3

def pedestrian_wants_to_cross():
    return grovepi.digitalRead(button) == 1  #retourner 1/True si le bouton est appuyé

def car_detected():
    return grovepi.digitalRead(magnetic_sensor) == 1  #retourner 1/True si la voiture est détectée 

try:
    while True:
        if pedestrian_wants_to_cross():
            # Allumer la LED verte pour indiquer que le piéton peut traverser
            red_led.on()        # Allumer la LED rouge de voiture
            green_led.off()     # Eteindre la LED vert de voiture
            green_led_2.on()    # Allumer la LED verte de piéton
            red_led_2.off()     # Eteindre la led rouge de piéton
            time.sleep(5)       # Attendre 5 secondes avant de vérifier à nouveau
            
        elif car_detected():
            red_led.off()       # Eteindre la LED rouge de voiture
            green_led.on()      # Allumer la LED rouge de voiture
            green_led_2.off()   # Eteindre la LED verte de piéton
            red_led_2.on()      # Allumer la LED rouge pour piéton
            time.sleep(5)       # Attendre 5 secondes avant de vérifier à nouveau
        else:
            # # laisser allumé la LED rouge si aucune action n'est requise
            red_led.on()        # Allumer la LED rouge de voiture
            green_led.off()     # Eteindre la LEd verte de voiture
            green_led_2.off()   # Eteindre la LED verte de piéton
            red_led_2.on()      # Allumer la LED rouge de piéton

            
except KeyboardInterrupt:
    # Éteindre les LEDs en cas d'interruption du programme
    red_led.off()      # Allumer la LED rouge de voiture
    green_led.off()    # Éteindre la LED verte de voiture
    green_led_2.off()  # Eteindre la LED verte de piéton
    red_led_2.off()    # Allumer la LED rouge de piéton
    print("Programme terminé")