from Class_Note import *
from envoi_valeurs import *


class Dico_modif :

    def __init__(self, liste_gam):
        self.liste_gam = liste_gam

    def modification(self,name, signe, gen, seq):
        actuel = gen["actuel"]
        gam = self.liste_gam[gen["gamme"] - 1]

        if name == "encodeur_PARAM":
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

        elif name == "encodeur_NOTE":
            note_pre = seq["pas{}".format(actuel[0])]["note"]
            lettre_pre, chiffre_pre = gam.separation(note_pre)

            if signe is None:
                chiffre_suiv = gam.next_chiffre(chiffre_pre)
                lettre_suiv = lettre_pre

            else:
                lettre_suiv = gam.next_lettre(lettre_pre, signe)
                chiffre_suiv = chiffre_pre

            note_suiv = lettre_suiv + str(chiffre_suiv)
            seq["pas{}".format(actuel[0])]["note"] = note_suiv

        elif name == "encodeur_GATE":
            if 0 <= round(seq["pas{}".format(actuel[0])]["gate"] + float("{}0.1".format(signe)), 2) <= 1:
                seq["pas{}".format(actuel[0])]["gate"] = round(seq["pas{}".format(actuel[0])]["gate"]
                                                               + float("{}0.1".format(signe)), 2)

        elif name == "encodeur_CV1":
            if 0 <= seq["pas{}".format(actuel[0])]["cv1"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv1"] += int("{}5".format(signe))

        elif name == "encodeur_CV2":
            if 0 <= seq["pas{}".format(actuel[0])]["cv2"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv2"] += int("{}5".format(signe))

        elif name == "encodeur_CV3":
            if 0 <= seq["pas{}".format(actuel[0])]["cv3"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv3"] += int("{}5".format(signe))

        elif name == "encodeur_CV4":
            if 0 <= seq["pas{}".format(actuel[0])]["cv4"] + int("{}5".format(signe)) <= 100:
                seq["pas{}".format(actuel[0])]["cv4"] += int("{}5".format(signe))

        return gen, seq
