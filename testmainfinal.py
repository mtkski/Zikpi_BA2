#Les imports
import RPi.GPIO as GPIO
from CONFIG_2 import *
from Class_Note import *
from gpiozero import Button
from gpiozero import RotaryEncoder
#from envoi_valeurs import *
from Affichageécran import Display
from envoi_valeurs import Melody
from Dico_modif import Action
from ouverture import démarrage
from signal import pause

# Pour déterminer quel système de numérotation des pins on utilise
GPIO.setmode(GPIO.BCM)

# Crée une liste d'objet pour les gammes
chromatique = Note(1)
majeur = Note(2)
mineur = Note(3)
liste_gam = [chromatique, majeur, mineur]

# définit l'objet melodie qui servira à l'envoit des valeurs
melodie = Melody()
démarrage()


        
melodie.joueSEQ
# définit l'objet affichage qui servira à l'affichage et affiche les valeurs du premier pas
affichage = Display()
affichage.all('pas1')


# définit l'objet action qui servira lors de l'actionnement des encodeurs et boutons
action = Action(liste_gam, melodie, affichage)

    #print(SEQ['pas1'])

    # Vérifie l'état des encodeurs et boutons à tout instant

bouton_play.when_pressed = action.play
bouton_playpas.when_pressed = action.playpas
bouton_next.when_pressed = action.next
bouton_prev.when_pressed = action.prev

encodeur_NOTE.when_rotated_clockwise = action.note_increase
encodeur_NOTE.when_rotated_counter_clockwise = action.note_decrease
encodeur_GATE.when_rotated_clockwise = action.gate_increase
encodeur_GATE.when_rotated_counter_clockwise = action.gate_decrease
encodeur_CV1.when_rotated_clockwise = action.cv1_decrease
encodeur_CV1.when_rotated_counter_clockwise = action.cv1_increase
encodeur_CV2.when_rotated_clockwise = action.cv2_decrease
encodeur_CV2.when_rotated_counter_clockwise = action.cv2_increase
encodeur_CV3.when_rotated_clockwise = action.cv3_decrease
encodeur_CV3.when_rotated_counter_clockwise = action.cv3_increase
encodeur_CV4.when_rotated_clockwise = action.cv4_decrease
encodeur_CV4.when_rotated_counter_clockwise = action.cv4_increase
encodeur_PARAM.when_rotated_clockwise = action.param_increase
encodeur_PARAM.when_rotated_counter_clockwise = action.param_decrease

bouton_NOTE.when_pressed = action.octave
bouton_GATE.when_pressed = action.silence
bouton_PARAM.when_pressed = action.param_chang

pause()
