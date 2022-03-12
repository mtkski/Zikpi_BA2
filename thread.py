#Les imports
import RPi.GPIO as GPIO
import threading
from CONFIG import Encodeur, Bouton, GEN, SEQ
from Class_Encoder import Encoder
from Class_Note import Note
from gpiozero import Button
from envoi_valeurs import *
from Affichageécran import *
from envoi_valeurs import *

global GEN, SEQ

# Pour déterminer quel système de numérotation des pins on utilise
GPIO.setmode(GPIO.BCM)

# Crée une liste d'objet pour les gammes
chromatique = Note(1)
majeur = Note(2)
mineur = Note(3)
liste_gam = [chromatique,majeur,mineur]

melodie = Melody()

bouton_play = Button(18)
bouton_playpas = Button(23)
bouton_next = Button(14)
bouton_prev = Button(15)

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
    
def pressed_play():
    thread = threading.Thread(target=melodie.joueSEQ)
    thread.start()
    
def pressed_playpas():
    melodie.jouePAS()

def pressed_next():
    GEN["actuel"][0] =  (GEN["actuel"][0] + 1) % (GEN["long"] +1)
    if GEN["actuel"][0] == 0:
        GEN["actuel"][0] = 1
    print(GEN["actuel"])
    affichervaleurs('pas' + str(GEN['actuel'][0]))
        
def pressed_prev():
    GEN["actuel"][0] -= 1
    if GEN["actuel"][0] == 0:
        GEN["actuel"][0] = GEN['long']
    print(GEN["actuel"])
    affichervaleurs('pas' + str(GEN['actuel'][0]))
    
print(GEN["actuel"])
# Boucle
while True:

    thread_list = []
    for encoder in encoder_dico.values():
        thread = threading.Thread(target=encoder.motion_sensor)
        thread.start()
        thread_list.append(thread)

    bouton_play.when_pressed = pressed_play
    bouton_playpas.when_pressed = pressed_playpas
    bouton_next.when_pressed = pressed_next
    bouton_prev.when_pressed = pressed_prev


    for encoder in encoder_dico.values():
        if encoder.etat == 'button encoder pressed':
            GEN, SEQ = encoder.action_spe(None, GEN, SEQ)
            print(SEQ['pas1'])
            affichervaleurs('pas' + str(GEN['actuel'][0]))

        elif encoder.etat == "rotated clockwise":
            GEN, SEQ = encoder.action_spe("+", GEN, SEQ)
            print(SEQ['pas1'])
            affichervaleurs('pas' + str(GEN['actuel'][0]))

        elif encoder.etat == "rotated counter-clockwise":
            GEN, SEQ = encoder.action_spe("-", GEN, SEQ)
            print(SEQ['pas1'])
            affichervaleurs('pas' + str(GEN['actuel'][0]))
