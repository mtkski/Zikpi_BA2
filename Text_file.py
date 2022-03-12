class Text_file :

    # IN : le nom du fichier sur lequel se retrouveront les informations (str)
    #       et le nom de l'encodeur si dans le cadre de la détection des encodeurs (str)
    # Ouvre le fichier, si le fichier n'existe pas en cree un
    # attribue le nom du fichier à l'objet
    def __init__(self,nom_fichier,encodeur_nom = None):
        open(nom_fichier,'w')
        self.nom_fichier = nom_fichier
        self.encodeur_nom = encodeur_nom

    # IN : L'état de l'encodeur (str) (ex : 'rotated clockwise')
    # Ouvre le fichier et l'efface (si le fichier n'existe pas en cree un)
    # et ajoute le nom de l'encodeur et son etat et ferme le fichier à la fin comme si c'était du code
    def ecriture_etat(self, etat):
        fichier = open(self.nom_fichier, 'w')
        fichier.write('dico_etat["{}"] = "{}"'.format(self.encodeur_nom,etat))
        fichier.close()

    # Efface le fichier et ferme le fichier
    def efface(self):
        fichier = open(self.nom_fichier, 'w')
        fichier.close()

    # IN : le dictionnaire des états des encodeurs
    # Ouvre le fichier en mode lecture et le ferme à la fin
    # lit le fichier texte et l'exécute comme du code
    # OUT : un dictionnaire avec en clef les noms des encodeurs et en valeur leur état
    def lecture_etat(self,dico_etat):
        fichier = open(self.nom_fichier, 'r')
        lignes = fichier.readlines()
        for ligne in lignes :
            exec(ligne)
        fichier.close()

        return dico_etat

    # IN : les dictionnaires de valeur GEN et SEQ (dict)
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
        GEN, SEQ = None, None
        for melodie in lignes :
            melodie = melodie[:-1] # retire le '\n'
            exec(melodie) # lit le str comme si s'était du code

        fichier.close()
        return GEN, SEQ