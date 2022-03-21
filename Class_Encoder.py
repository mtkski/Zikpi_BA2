#les imports
from Affichageécran import *
from Class_Note import *
import RPi.GPIO as GPIO
from time import sleep
from envoi_valeurs import *


# Classe définissant les encodeurs
class Encoder:

    # IN : le nom de l'encodeur et le numéro des pins clk, dt et sw (None par défaut si pas de sw)
    # Définit l'objet encodeur, PreValue et LastValue sont des valeurs utilent pour la méthode "motion_sensor"
    def __init__(self, name, liste_gam, fichier_dico, clk, dt, sw=None, ):
        self.name = name
        self.liste_gam = liste_gam
        #self.fichier_dico = fichier_dico
        self.etat = None
        self.clk = clk
        self.dt = dt
        self.sw = sw
        if sw is not None:
            self.PreValue = GPIO.input(sw)
            print(self.name, ":", [GPIO.input(clk), GPIO.input(dt), GPIO.input(sw)]) # print
        else :
            print(self.name, ":", [GPIO.input(clk), GPIO.input(dt)]) # print
        self.LastValue = [GPIO.input(clk), GPIO.input(dt)]


    # Détecte les actions sur les encodeurs (tourner à gauche/droite et utilisation du bouton poussoir)
    def motion_sensor(self):
        global GEN, SEQ
        #fichier = self.fichier_dico[self.name]
        self.etat = None
        check = 0
        clkvalue = GPIO.input(self.clk)
        dtvalue = GPIO.input(self.dt)
        actualvalue = [clkvalue, dtvalue]

        if self.sw is not None:
            buttonvalue = GPIO.input(self.sw)
            if buttonvalue != self.PreValue:
                while not buttonvalue == 1:
                    buttonvalue = GPIO.input(self.sw)

                self.etat = 'button encoder pressed'
                #fichier.ecriture_etat('Button encoder pressed')
                print(self.name, 'Button encoder pressed') # print
                sleep(0.2)

        if actualvalue != self.LastValue:
            if clkvalue == 0 and dtvalue == 1:
                while not (clkvalue == 1 and dtvalue == 1):
                    check += 1
                    clkvalue = GPIO.input(self.clk)
                    dtvalue = GPIO.input(self.dt)

                if check > 1000 :
                    self.etat = 'rotated clockwise'
                    #fichier.ecriture_etat('rotated clockwise')
                    print(self.name, 'rotated clockwise') # print
                    sleep(0.2)

            elif clkvalue == 1 and dtvalue == 0:
                while not (clkvalue == 1 and dtvalue == 1):
                    check += 1
                    clkvalue = GPIO.input(self.clk)
                    dtvalue = GPIO.input(self.dt)

                if check > 1000 :
                    self.etat = 'rotated counter-clockwise'
                    #fichier.ecriture_etat('rotated counter-clockwise')
                    print(self.name, 'rotated counter-clockwise') # print
                    sleep(0.2)

    # IN : le signe de la modification +/- qui change si on tourne l'encodeur à gauche ou à droite
    #       et les dictionnaires de valeur GEN et SEQ (voir CONFIG.py)
    # Fait les actions spécifique aux encodeurs. Par exemple en modifiant les valeurs dans les dictionnaires de valeur GEN et SEQ
    def action_spe(self, signe, gen, seq):
        actuel = gen["actuel"]
        gam = self.liste_gam[gen["gamme"]-1]

        if self.name == "encodeur_PARAM":
            if signe is None:
                print(gen['actuel'])
                gen["actuel"][1] = (gen["actuel"][1] + 1) % 3

            elif actuel[1] == 1:
                if 0 <= gen["long"] + float("{}1".format(signe)) <= 64:
                    if actuel[0] > gen["long"] + float("{}1".format(signe)):
                        gen["long"] += float("{}1".format(signe))

            elif actuel[1] == 2:
                if 0 <= gen["bpm"] + float("{}1".format(signe)) <= 500:
                    gen["bpm"] += float("{}1".format(signe))

            elif actuel[1] == 3:
                if 1 <= gen["gam"] + float("{}1".format(signe)) <= 3:
                    gen["gam"] += float("{}1".format(signe))

        elif self.name == "encodeur_NOTE":
            note_pre = seq["pas{}".format(actuel[0])]["note"]
            lettre_pre, chiffre_pre = gam.separation(note_pre)

            if signe is None:
                chiffre_suiv = gam.next_chiffre(chiffre_pre)
                lettre_suiv = lettre_pre

            else:
                lettre_suiv = gam.next_lettre(lettre_pre,signe)
                chiffre_suiv = chiffre_pre

            note_suiv = lettre_suiv + str(chiffre_suiv)
            seq["pas{}".format(actuel[0])]["note"] = note_suiv
            

        elif self.name == "encodeur_GATE":
            if 0 <= round(seq["pas{}".format(actuel[0])]["gate"] + float("{}0.1".format(signe)),2) <= 1:
                seq["pas{}".format(actuel[0])]["gate"] =  round(seq["pas{}".format(actuel[0])]["gate"]
                                                                + float("{}0.1".format(signe)),2)

        elif self.name == "encodeur_CV1":
            if 0 <= seq["pas{}".format(actuel[0])]["cv1"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv1"] += int("{}5".format(signe))

        elif self.name == "encodeur_CV2":
            if 0 <= seq["pas{}".format(actuel[0])]["cv2"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv2"] += int("{}5".format(signe))

        elif self.name == "encodeur_CV3":
            if 0 <= seq["pas{}".format(actuel[0])]["cv3"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv3"] += int("{}5".format(signe))


        elif self.name == "encodeur_CV4":
            if 0 <= seq["pas{}".format(actuel[0])]["cv4"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv4"] += int("{}5".format(signe))


        return gen, seq