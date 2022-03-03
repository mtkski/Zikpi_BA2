# Classe définissant les encodeurs
class Encoder:

    # IN : le nom de l'encodeur et le numéro des pins clk, dt et sw (None par défaut si pas de sw)
    # Définit l'objet encodeur, PreValue et LastValue sont des valeurs utilent pour la méthode "motion_sensor"
    def __init__(self, name, liste_gam, clk, dt, sw=None, ):
        self.name = name
        self.liste_gam = liste_gam
        self.clk = clk
        self.dt = dt
        self.sw = sw
        if sw is not None:
            self.PreValue = GPIO.input(sw)
        self.LastValue = [GPIO.input(clk), GPIO.input(dt)]

    # Détecte les actions sur les encodeurs (tourner à gauche/droite et utilisation du bouton poussoir)
    def motion_sensor(self):
        clkvalue = GPIO.input(self.clk)
        dtvalue = GPIO.input(self.dt)
        actualvalue = [clkvalue, dtvalue]

        if self.sw is not None:
            buttonvalue = GPIO.input(self.sw)
            if buttonvalue != self.PreValue:
                while not buttonvalue == 0:
                    buttonvalue = GPIO.input(self.sw)
                sleep(0.2)
                return "button pressed"

        if actualvalue != self.LastValue:
            if clkvalue == 0 and dtvalue == 1:
                while not (clkvalue == 1 and dtvalue == 1):
                    clkvalue = GPIO.input(self.clk)
                    dtvalue = GPIO.input(self.dt)
                return "rotated clockwise"

            elif clkvalue == 1 and dtvalue == 0:
                while not (clkvalue == 1 and dtvalue == 1):
                    clkvalue = GPIO.input(self.clk)
                    dtvalue = GPIO.input(self.dt)
                return "rotated counter-clockwise"

    # IN : le signe de la modification +/- qui change si on tourne l'encodeur à gauche ou à droite
    #       et les dictionnaires de valeur GEN et SEQ (voir CONFIG.py)
    # Modifie les valeurs dans les dictionnaires de valeur GEN et SEQ
    def dictionary_modification(self, signe, gen, seq):
        actuel = gen["actuel"]
        gam = self.liste_gam[gen["gam"]-1]

        if self.name == "encodeur_PARAM":
            if signe is None:
                gen["actuel"][1] = (gen["actuel"][1] + 1) % 3

            elif actuel[1] == 1:
                if 0 <= gen["long"] + float("{}1".format(signe)) <= 64:
                    if actuel[0] > gen["long"] + float("{}1".format(signe)):
                        gen["long"] += float("{}1".format(signe))

            elif actuel[1] == 2:
                if 0 <= gen["bpm"] + float("{}25".format(signe)) <= 500:
                    gen["bpm"] += float("{}25".format(signe))

            elif actuel[1] == 3:
                if 1 <= gen["gam"] + float("{}1".format(signe)) <= 3:
                    gen["gam"] += float("{}1".format(signe))

        elif self.name == "encodeur_NOTE":
            note_pre = seq["pas{}".format(actuel[0])]["note"]
            lettre_pre, chiffre_pre = Note.separation(note_pre)

            if signe is None:
                chiffre_suiv = Note.next_chiffre(chiffre_pre)

            else:
                lettre_suiv = Note.next_lettre(lettre_pre,signe)

            note_suiv = lettre_suiv + str(chiffre_suiv)
            seq["pas{}".format(actuel[0])]["note"] = note_suiv

        elif self.name == "encodeur_GATE":
            if 5 <= seq["pas{}".format(actuel[0])]["gate"] + float("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["gate"] += float("{}5".format(signe))

        elif self.name == "encodeur_CV1":
            if 5 <= seq["pas{}".format(actuel[0])]["cv1"] + float("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv1"] += float("{}5".format(signe))

        elif self.name == "encodeur_CV2":
            if 5 <= seq["pas{}".format(actuel[0])]["cv2"] + float("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv2"] += float("{}5".format(signe))

        elif self.name == "encodeur_CV3":
            if 5 <= seq["pas{}".format(actuel[0])]["cv3"] + float("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv3"] += float("{}5".format(signe))

        elif self.name == "encodeur_CV4":
            if 5 <= seq["pas{}".format(actuel[0])]["cv4"] + float("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv4"] += float("{}5".format(signe))

        return gen, seq
