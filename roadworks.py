# Import the needed modules
import time
from gpiozero import LED

led_red_1 = LED(17)  # Premier feu rouge
led_green_1 = LED(18)  # Premier feu vert
led_red_2 = LED(22) # Second feu rouge
led_green_2 = LED(23)  # Second feu vert


def switch_lights():
    """Fonction pour alterner les feux entre rouge et vert."""
    while True:
        # Premier côté passe au vert
        led_green_1.on()  # First Green LED ON
        led_red_1.off() # First Red LED OFF
        led_green_2.off()  #Second Green LED OFF
        led_red_2.on()  # Second Red LED ON
        
        time.sleep(10)  # Laissez le premier côté vert pendant 10 secondes
        
        
        # Attendez 5 secondes supplémentaires pour les dernières voitures
        led_green_1.off()  # First Green LED OFF
        led_red_1.on()  # First Red LED ON
        time.sleep(5)
        
         # Second côté passe au vert
        led_green_2.on()  #Second Green LED ON
        led_red_2.off() # Second Red LED OFF
        led_green_1.off() # First Green LED OFF
        led_red_1.on()  # First Red LED ON

        time.sleep(10)  # Laissez le second côté vert pendant 10 secondes
        
         # Attendez 5 secondes supplémentaires pour les dernières voitures
        led_green_2.off() # First Green LED OFF
        led_red_2.on()  # First Red LED ON
        time.sleep(5)
        
       
try:
    switch_lights()
    
except KeyboardInterrupt:
    led_green_1.off()  # First Green LED OFF
    led_red_1.off()  # First Red LED OFF
    led_green_2.off()  #Second Green LED OFF
    led_red_2.off()  # Second Red LED OFF
            
    print("Program a été arrété par utilisateur.")

        # Turn both LEDs off before stopping
            