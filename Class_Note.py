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
    
    # IN : la note
    # sépare la lettre et le chiffre de la note
    # OUT : Lettre et chiffre de la note (ex : "c" et 1)
    def separation(self,note):
        if len(note) == 3:
            lettre = note[0] + note[1]
            chiffre = int(note[2])

        elif len(note) == 2:
            lettre = note[0]
            chiffre = int(note[1])

        return lettre, chiffre
    
    # IN : la lettre de la note précédante et le signe (+ ou -) en fonction de la rotation de l'encodeur
    # Donne la lettre suivante par rapport à la liste de la gamme
    # OUT : La lettre de la note suivante
    def next_lettre(self,lettre_pre,signe):
        position_pre = self.liste_lettre.index(lettre_pre)
        len_liste_lettre = len(self.liste_lettre)
        position_suiv = (position_pre + int("{}1".format(signe))) % len_liste_lettre

        return self.liste_lettre[position_suiv]
    
    # IN : Le chiffre de la note précédante
    # Donne le chiffre suivant (modulo)
    # OUT : le chiffre de la note suivante
    def next_chiffre(self,chiffre_pre):
        chiffre_suiv = (chiffre_pre + 1) % 6
        if chiffre_suiv == 0 :
            chiffre_suiv +=1

        return chiffre_suiv
    
    # IN: Lettre de la note et chiffre de l'octave
    # Assemble la lettre et le chiffre
    # Renvoie le symbole de la note
    def assemblage(self, lettre, chiffre):
        symbole = lettre + str(chiffre)
        return symbole

    # IN : le symbole de la note
    # Construit un dictionnaire avec les symboles comme clé et les valeurs dac en valeur dico. Cherche ensuite le symbole entré dans la fonction et renvoie sa valeur
    # OUT : Valeur DAC de la note
    def traduction_note_DAC(self, symbole):
        dico_note = {}

        for i in range(1,61,1):
            Lettre_note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
            octave = int((i) / 12 + 0.99)
            lettre = i % 12
            valeur_dac = i * (4096/60)
            dico_note[Lettre_note[lettre - 1] + str(octave)] = valeur_dac

        return dico_note.get(symbole)
