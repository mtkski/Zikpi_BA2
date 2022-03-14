#Les imports
import RPi.GPIO as GPIO
import threading
from CONFIG_2 import *
from Class_Note import Note
from gpiozero import Button
from gpiozero import RotaryEncoder
from Dico_modif import *
from envoi_valeurs import *
from Affichageécran import *
from envoi_valeurs import *
from Text_file import *

# Pour déterminer quel système de numérotation des pins on utilise
GPIO.setmode(GPIO.BCM)

# Crée une liste d'objet pour les gammes
chromatique = Note(1)
majeur = Note(2)
mineur = Note(3)
liste_gam = [chromatique,majeur,mineur]

modif = Dico_modif(liste_gam)

melodie = Melody()

# Crée une liste d'objet encoder et configure chaque canal comme entrée ou sortie pour les encodeurs
encoder_dico = {}
button_encoder_dico = {}
modification
for encoder_name in Encodeur.keys():
    CLK = Encodeur[encoder_name][0]
    DT = Encodeur[encoder_name][1]
    SW = Encodeur[encoder_name][2]
    GPIO.setup(CLK, GPIO.IN)
    GPIO.setup(DT, GPIO.IN)
    if SW is not None:
        GPIO.setup(SW, GPIO.IN)
        button = Button(SW)
        button_encoder_dico[encoder_name] = button
    encoder = RotaryEncoder(CLK,DT)
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
    print(GEN["actuel"]) # print
    affichervaleurs('pas' + str(GEN['actuel'][0]))
        
def pressed_prev():
    GEN["actuel"][0] -= 1
    if GEN["actuel"][0] == 0:
        GEN["actuel"][0] = GEN['long']
    print(GEN["actuel"]) # print
    affichervaleurs('pas' + str(GEN['actuel'][0]))
    
print(GEN["actuel"]) # print


def rotated_clockwise(nom) :
    GEN, SEQ = modif.modification(nom,'+', GEN, SEQ)
    print('clockwise')

def rotated_counter_clockwise(nom) :
    GEN, SEQ = encoder.action_spe(nom,'-', GEN, SEQ)
    print('counter_clockwise')

def encoder_pressed(nom) :
    GEN, SEQ = encoder.action_spe(nom,None, GEN, SEQ)
    print('encoder pressed')



# Boucle
while True:


    bouton_play.when_pressed = pressed_play
    bouton_playpas.when_pressed = pressed_playpas
    bouton_next.when_pressed = pressed_next
    bouton_prev.when_pressed = pressed_prev

    encodeur_NOTE.when_rotated_clockwise = rotated_clockwise("encodeur_NOTE")
    encodeur_NOTE.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_NOTE")
    encodeur_GATE.when_rotated_clockwise = rotated_clockwise("encodeur_GATE")
    encodeur_GATE.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_GATE")
    encodeur_CV1.when_rotated_clockwise = rotated_clockwise("encodeur_CV1")
    encodeur_CV1.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_CV1")
    encodeur_CV2.when_rotated_clockwise = rotated_clockwise("encodeur_CV2")
    encodeur_CV2.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_CV2")
    encodeur_CV3.when_rotated_clockwise = rotated_clockwise("encodeur_CV3")
    encodeur_CV3.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_CV3")
    encodeur_CV4.when_rotated_clockwise = rotated_clockwise("encodeur_CV4")
    encodeur_CV4.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_CV4")
    encodeur_PARAM.when_rotated_clockwise = rotated_clockwise("encodeur_PARAM")
    encodeur_PARAM.when_rotated_counter_clockwise = rotated_counter_clockwise("encodeur_PARAM")

    bouton_NOTE.when_pressed = encoder_pressed("encodeur_NOTE")
    bouton_GATE.when_pressed = encoder_pressed("encodeur_GATE")
    bouton_PARAM.when_pressed = encoder_pressed("encodeur_PARAM")

