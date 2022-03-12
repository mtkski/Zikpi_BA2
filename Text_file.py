
class Text_file :

     # Ouvre le fichier, si le fichier n'existe pas en cree un
     # attribue le nom du fichier à l'objet
    def __init__(self,nom_fichier):
        open(nom_fichier,'w')
        self.nom_fichier = nom_fichier

    # IN : nom de l'encodeur et son etat (ex : 'encodeur_NOTE' et 'rotated clockwise')
    # Ouvre le fichier et ajoute le nom de l'encodeur et son etat et ferme le fichier à la fin
    def ecriture_etat(self,encodeur_nom, etat):
        fichier = open(self.nom_fichier, 'a')
        fichier.write(encodeur_nom + ' : ' + etat + '\n')
        fichier.close()

    # Efface le fichier et ferme le fichier
    def efface(self):
        fichier = open(self.nom_fichier, 'w')
        fichier.close()

    # Ouvre le fichier en mode lecture et le ferme à la fin
    # lit le fichier et retourne le nom de l'encodeur et son état
    # OUT : un dictionnaire avec en clef les noms des encodeurs et en valeur leur état
    def lecture_etat(self):
        fichier = open(self.nom_fichier, 'r')
        lignes = fichier.readlines()
        liste = []
        for ligne in lignes :
            l = ligne[:-1] # retire le '\n'
            liste.append(l)

        dico_etat = {}
        for element in liste:
            a = 0
            encoder_nom = ''
            etat = ''
            for caract in element:
                if caract in ' : ':
                    a = 1
                elif a == 0:
                    encoder_nom += caract
                elif a == 1:
                    etat += caract
            dico_etat[encoder_nom] = etat
        fichier.close()

        return dico_etat

    # IN : les dictionnaires de valeur GEN et SEQ
    # Ouvre le fichier et l'efface (si le fichier n'existe pas il le crée) et à la fin ferme le fichier
    # Ecris dans le fichier les dictionnaires de valeur GEN et SEQ
    def save_melodie(self,gen,seq):
        fichier = open(self.nom_fichier, 'w')
        fichier.write('GEN = ' + str(gen) + '\n')
        fichier.write('SEQ = '+ str(seq) + '\n')
        fichier.close()

    # Ouvre le fichier en mode lecture et le ferme à la fin
    # reprend du fichier les dictionnaires de valeur GEN et SEQ sauvés
    # OUT : tuple comprenant les dictionnaires de valeur GEN et SEQ
    def reprise_melodie_sauvée(self):
        fichier = open(self.nom_fichier, 'r')
        lignes = fichier.readlines()
        for melodie in lignes :
            melodie = melodie[:-1] # retire le '\n'
            exec(melodie) # lit le str comme si s'était du code

        fichier.close()
        return GEN, SEQ
