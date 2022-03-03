class Note:
    def __init__(self,num_gam):
        if num_gam == 1:
            self.name = "Chromatique"
            self.liste_lettre = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        elif num_gam == 2:
            self.name = "Majeur"
            self.liste_lettre = ["C", "D", "E", "F", "G", "A", "B"]
        elif num_gam == 3:
            self.name = "Mineur"
            self.liste_lettre = ["C", "D", "D#", "F", "G", "G#", "A#"]

    def separation(self,note_pre):
        if len(note_pre) == 3:
            lettre_pre = note_pre[0] + note_pre[1]
            chiffre_pre = int(note_pre[2])

        elif len(note_pre) == 2:
            lettre_pre = note_pre[0]
            chiffre_pre = int(note_pre[1])

        return lettre_pre, chiffre_pre

    def next_lettre(self,lettre_pre,signe):
        position_pre = self.liste_lettre.index(lettre_pre)
        len_liste_lettre = len(self.liste_lettre)
        position_suiv = (position_pre + int("{}1".format(signe))) % len_liste_lettre

        return self.liste_lettre[position_suiv]

    def next_chiffre(self,chiffre_pre):
        chiffre_suiv = (chiffre_pre + 1) % 6
        if chiffre_suiv == 0 :
            chiffre_suiv +=1

        return chiffre_suiv
