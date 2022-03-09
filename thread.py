#Les imports
import RPi.GPIO as GPIO
import threading
from CONFIG import Encodeur, Bouton, GEN, SEQ
from Class_Button import Button
from Class_Encoder import Encoder
from Class_Note import Note

global GEN, SEQ

# Pour déterminer quel système de numérotation des pins on utilise
GPIO.setmode(GPIO.BCM)

# Crée une liste d'objet pour les gammess
chromatique = Note(1)
majeur = Note(2)
mineur = Note(3)
liste_gam = [chromatique,majeur,mineur]

# Crée une liste d'objet button et configure chaque canal comme entrée ou sortie pour les boutons
button_dico = {}
for button_name in Bouton.keys():
    PIN = Bouton[button_name]
    GPIO.setup(PIN, GPIO.IN)
    button = Button(button_name, PIN)
    button_dico[button_name] = button

# Crée une liste d'objet encoder et configure chaque canal comme entrée ou sortie pour les encodeurs
encoder_dico = {}
for encoder_name in Encodeur.keys():
    CLK = Encodeur[encoder_name][0]
    DT = Encodeur[encoder_name][1]
    SW = Encodeur[encoder_name][2]
    GPIO.setup(CLK, GPIO.IN)
    GPIO.setup(DT, GPIO.IN)
    if SW is not None:
        GPIO.setup(SW, GPIO.IN)
    encoder = Encoder(encoder_name, liste_gam, CLK, DT, SW)
    encoder_dico[encoder_name] = encoder

# Boucle
while True:

    thread_list = []
    for encodeur_nom in encoder_dico.keys():
        thread = threading.Thread(target=encoder_dico[encodeur_nom].motion_sensor)
        thread.start()
        thread_list.append(thread)

    for bouton_nom in button_dico.keys():
        thread = threading.Thread(target=button_dico[bouton_nom].motion_sensor)
        thread.start()
        thread_list.append(thread)

    for thread in thread_list :
        thread.join()
