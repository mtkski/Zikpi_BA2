#Les imports
import RPi.GPIO as GPIO
from CONFIG import Encodeur, Bouton, GEN, SEQ
from Class_Button import Button
from Class_Encoder import Encoder
from Class_Note import Note

# Pour déterminer quel système de numérotation des pins on utilise
GPIO.setmode(GPIO.BCM)

# Crée une liste d'objet pour les gammess
chromatique = Note(1)
majeur = Note(2)
mineur = Note(3)
liste_gam = [chromatique,majeur,mineur]

# Crée une liste d'objet button et configure chaque canal comme entrée ou sortie pour les boutons
button_list = []
for button_name in Bouton.keys():
    PIN = Bouton[button_name]
    GPIO.setup(PIN, GPIO.IN)
    button = Button(button_name, PIN)
    button_list.append(button)

# Crée une liste d'objet encoder et configure chaque canal comme entrée ou sortie pour les encodeurs
encoder_list = []
for encoder_name in Encodeur.keys():
    CLK = Encodeur[encoder_name][0]
    DT = Encodeur[encoder_name][1]
    SW = Encodeur[encoder_name][2]
    GPIO.setup(CLK, GPIO.IN)
    GPIO.setup(DT, GPIO.IN)
    if SW is not None:
        GPIO.setup(SW, GPIO.IN)
    encoder = Encoder(encoder_name, liste_gam, CLK, DT, SW)
    encoder_list.append(encoder)


# Boucle
while True:

    # Prise de valeur
    for encoder in encoder_list:
        if encoder.motion_sensor() == "button pressed":
            GEN, SEQ = encoder.dictionary_modification(None, GEN, SEQ)

        elif encoder.motion_sensor() == "rotated clockwise":
            GEN, SEQ = encoder.dictionary_modification("+", GEN, SEQ)

        elif encoder.motion_sensor() == "rotated counter-clockwise":
            GEN, SEQ = encoder.dictionary_modification("-", GEN, SEQ)

    for button in button_list:
        if button.motion_sensor() == "button pressed":
            GEN = button.dictionary_modification(GEN)

