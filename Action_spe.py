import threading

class Action:

    global GEN, SEQ

    def __init__(self, liste_gam, melodie, affichage):
        self.liste_gam = liste_gam
        self.melodie = melodie
        self.affichage = affichage

    def param_chang(self):
        GEN["actuel"][1] = (GEN["actuel"][1] + 1) % 3

        self.affichage.param('pas' + str(GEN['actuel'][0]))

    def param_increase(self):
        actuel = GEN["actuel"]
        num_param = actuel[1]
        step = 1
        long_max = 64
        bpm_max = 500
        gam_max = 3

        if num_param == 0:
            if GEN["long"] + step <= long_max:
                GEN["long"] += step

                self.affichage.param('pas' + str(GEN['actuel'][0]))

        elif num_param == 1:
            if GEN["bpm"] + step <= bpm_max:
                GEN["bpm"] += step

                self.affichage.param('pas' + str(GEN['actuel'][0]))

        elif num_param == 2:
            if GEN["gamme"] + step <= gam_max:
                GEN["gamme"] += step

                self.affichage.param('pas' + str(GEN['actuel'][0]))

    def param_decrease(self):
        actuel = GEN["actuel"]
        num_pas = actuel[0]
        num_param = actuel[1]
        step = 1
        long_min = 64
        bpm_min = 500
        gam_min = 3

        if num_param == 0:
            if GEN["long"] - step >= long_min:
                if num_pas <= GEN["long"] - step:
                    GEN["long"] -= step

                    self.affichage.param('pas' + str(GEN['actuel'][0]))

        elif num_param == 1:
            if GEN["bpm"] - step >= bpm_min:
                GEN["bpm"] -= step

                self.affichage.param('pas' + str(GEN['actuel'][0]))

        elif num_param == 2:
            if GEN["gamme"] - step >= gam_min:
                GEN["gamme"] -= step

                self.affichage.param('pas' + str(GEN['actuel'][0]))

    def note_increase(self):
        actuel = GEN["actuel"]
        gam = self.liste_gam[GEN["gamme"] - 1]

        note_pre = SEQ["pas{}".format(actuel[0])]["note"]
        lettre_pre, chiffre = gam.separation(note_pre)

        lettre_suiv = gam.next_lettre(lettre_pre, '+')

        note_suiv = lettre_suiv + str(chiffre)
        SEQ["pas{}".format(actuel[0])]["note"] = note_suiv

        self.affichage.note('pas' + str(GEN['actuel'][0]))

    def note_decrease(self):
        actuel = GEN["actuel"]
        gam = self.liste_gam[GEN["gamme"] - 1]

        note_pre = SEQ["pas{}".format(actuel[0])]["note"]
        lettre_pre, chiffre = gam.separation(note_pre)

        lettre_suiv = gam.next_lettre(lettre_pre, '-')

        note_suiv = lettre_suiv + str(chiffre)
        SEQ["pas{}".format(actuel[0])]["note"] = note_suiv

        self.affichage.note('pas' + str(GEN['actuel'][0]))

    def octave(self):
        actuel = GEN["actuel"]
        gam = self.liste_gam[GEN["gamme"] - 1]

        note_pre = SEQ["pas{}".format(actuel[0])]["note"]
        lettre, chiffre_pre = gam.separation(note_pre)

        chiffre_suiv = gam.next_chiffre(chiffre_pre)

        note_suiv = lettre + str(chiffre_suiv)
        SEQ["pas{}".format(actuel[0])]["note"] = note_suiv

        self.affichage.note('pas' + str(GEN['actuel'][0]))

    def gate_increase(self):
        actuel = GEN["actuel"]
        step = 0.1
        gate_max = 1

        if SEQ["pas{}".format(actuel[0])]["gate"] + step <= gate_max:
            SEQ["pas{}".format(actuel[0])]["gate"] += step

            self.affichage.gate('pas' + str(GEN['actuel'][0]))

    def gate_decrease(self):
        actuel = GEN["actuel"]
        step = 0.1
        gate_min = 0

        if SEQ["pas{}".format(actuel[0])]["gate"] - step >= gate_min:
            SEQ["pas{}".format(actuel[0])]["gate"] -= step

            self.affichage.gate('pas' + str(GEN['actuel'][0]))

    def silence(self):
        actuel = GEN["actuel"]
        SEQ["pas{}".format(actuel[0])]["gate"] = 0

        self.affichage.gate('pas' + str(GEN['actuel'][0]))

    def cv1_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv1_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv1"] + step <= cv1_max:
            SEQ["pas{}".format(actuel[0])]["cv1"] += step

            self.affichage.cv1('pas' + str(GEN['actuel'][0]))

    def cv1_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv1_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv1"] - step >= cv1_min:
            SEQ["pas{}".format(actuel[0])]["cv1"] -= step

            self.affichage.cv1('pas' + str(GEN['actuel'][0]))

    def cv2_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv2_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv2"] + step <= cv2_max:
            SEQ["pas{}".format(actuel[0])]["cv2"] += step

            self.affichage.cv2('pas' + str(GEN['actuel'][0]))

    def cv2_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv2_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv2"] - step >= cv2_min:
            SEQ["pas{}".format(actuel[0])]["cv2"] -= step

            self.affichage.cv2('pas' + str(GEN['actuel'][0]))

    def cv3_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv3_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv3"] + step <= cv3_max:
            SEQ["pas{}".format(actuel[0])]["cv3"] += step

            self.affichage.cv3('pas' + str(GEN['actuel'][0]))

    def cv3_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv3_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv3"] - step >= cv3_min:
            SEQ["pas{}".format(actuel[0])]["cv3"] -= step
            self.affichage.cv3('pas' + str(GEN['actuel'][0]))

    def cv4_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv4_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv4"] + step <= cv4_max:
            SEQ["pas{}".format(actuel[0])]["cv4"] += step

            self.affichage.cv4('pas' + str(GEN['actuel'][0]))

    def cv4_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv4_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv4"] - step >= cv4_min:
            SEQ["pas{}".format(actuel[0])]["cv4"] -= step

            self.affichage.cv4('pas' + str(GEN['actuel'][0]))

    def play(self):
        thread = threading.Thread(target=self.melodie.joueSEQ)
        thread.start()

    def playpas(self):
        self.melodie.jouePAS()

    def next(self):
        GEN["actuel"][0] = (GEN["actuel"][0] + 1) % (GEN["long"] + 1)
        if GEN["actuel"][0] == 0:
            GEN["actuel"][0] = 1

        self.affichage.all('pas' + str(GEN['actuel'][0]))

    def prev(self):
        GEN["actuel"][0] -= 1
        if GEN["actuel"][0] == 0:
            GEN["actuel"][0] = GEN['long']

        self.affichage.all('pas' + str(GEN['actuel'][0]))
