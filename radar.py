import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


import grovepi
import time

# Définir les numéros de broches GPIO
sensor1_pin = 7  # Premier capteur
sensor2_pin = 8  # Deuxième capteur

grovepi.pinMode(sensor1_pin, "INPUT")
grovepi.pinMode(sensor2_pin, "INPUT")

# Variables pour le calcul de la vitesse
start_time = 0
end_time = 0
distance_between_sensors = 20 # cm, distance entre les capteurs

#fonction qui renvoie le temps en secondes
def read_sensor(pin):  
    while grovepi.digitalRead(pin) == 0:  #attendre jusqu'à ce que le capteur détecte quelque chose et renvoie une valeur différente de zéro.
        pass
    return time.time()     

try:
    print("Faites passer l'objet métallique à travers les capteurs.")
    
    while True:
        start_time = read_sensor(sensor1_pin)
        end_time = read_sensor(sensor2_pin)

        # Calcul de la vitesse
        elapsed_time = end_time - start_time
        speed = distance_between_sensors / elapsed_time

        print(f"La vitesse de la voiture: {speed:.4f} cm/s")

        if speed > 25:
        
         # Paramètres du serveur SMTP
            smtp_server = 'smtp.g-solutions.ch'     # SMTP server address
            smtp_port = 587                        # SMTP server port, typiquement 587 pour TLS
            smtp_username = 'hesso@g-solutions.ch'  # votre adresse email
            smtp_password = 'Abcd123456'            # votre mot de passe

            # Destinataire
            to_address = 'detinataire@live.com'       # adresse email du destinataire

            # Création de l'objet MIMEMultipart
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = to_address
            msg['Subject'] = 'Excès de vitesse détecté'

            # Corps du message en HTML
            html_message = """
            <html>
              <head></head>
              <body>
              <p>Bonjour,<br>
                   Vous avez dépassé la limite de vitesse autorisée.<br>
                <p>Veuillez consulter le fichier ci-joint qui définit le montant de l'amende.</p>
                 <a href="http://www.twint.ch/fr/">Lien pour la facturation</a>
                <img src="https://www.hevs.ch/_nuxt/img/logo_hesso.9af1d79.svg">
              </body>
            </html>
            """

            # Ajouter le corps HTML au message
            msg.attach(MIMEText(html_message, 'html')) #attache le message de type htlm au message dans la variale mimemultipart



            # Pièce jointe
            filename = '/home/pi/Desktop/amende.txt' #CHANGER
            attachment = open(filename, 'rb') #open the file on binary format for reading 

            part = MIMEBase('application', 'octet-stream') # c'est là ou on met la piece attachée
            part.set_payload((attachment).read())
            encoders.encode_base64(part) 
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(part) # on attache la piece la piece join au message 



            #pour envoyer le message
            # Connexion au serveur SMTP
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            # Envoi de l'e-mail
            server.sendmail(smtp_username, to_address, msg.as_string())

            # Fermeture de la connexion
            server.quit()

            print("Email envoyé avec succès!")
                
        


except KeyboardInterrupt:
    print("Programme terminé.")