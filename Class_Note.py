# Classe pour les changements de note par rapport à la gamme
class Note:
    # IN : le numéro de la gamme [1,3]
    # Définit le nom et la liste associé à la gamme
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
    
    # IN : la note précedante
    # sépare la lettre et le chiffre de la note
    def separation(self,note_pre):
        if len(note_pre) == 3:
            lettre_pre = note_pre[0] + note_pre[1]
            chiffre_pre = int(note_pre[2])

        elif len(note_pre) == 2:
            lettre_pre = note_pre[0]
            chiffre_pre = int(note_pre[1])

        return lettre_pre, chiffre_pre
    
    # IN : la lettre de la note précédante et le signe (+ ou -) en fonction de la rotation de l'encodeur
    # Donne la lettre suivante par rapport à la liste de la gamme
    def next_lettre(self,lettre_pre,signe):
        position_pre = self.liste_lettre.index(lettre_pre)
        len_liste_lettre = len(self.liste_lettre)
        position_suiv = (position_pre + int("{}1".format(signe))) % len_liste_lettre

        return self.liste_lettre[position_suiv]
    
    # IN : Le chiffre de la note précédante
    # Donne le chiffre suivant (modulo)
    def next_chiffre(self,chiffre_pre):
        chiffre_suiv = (chiffre_pre + 1) % 6
        if chiffre_suiv == 0 :
            chiffre_suiv +=1

        return chiffre_suiv
