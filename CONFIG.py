
max = 64
SEQ = {}
for i in range(1,max+1):
    PARAM = {"note":'C2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM

# SEQ['pas1']['note'] = 1 pour modifier (exemple)
# actuel = [num du pas, numéro du paramètre de l'encodeur PARAM (1:long, 2:bpm, 3:gamme)]

GEN = {"long":8, "bpm":120, "gamme":1, "actuel" : [1,1]}

# Définit les pins utilisés par les encodeurs
Encodeur = {
    "encodeur_NOTE" : [10,9,11],
    "encodeur_GATE" : [5,6,None],
    "encodeur_CV1" : [20,21,None],
    "encodeur_CV2" : [12,16,None],
    "encodeur_CV3" : [8,7,None],
    "encodeur_CV4" : [24,25,None],
    "encodeur_PARAM" : [13,19,26]
    }

# Définit les pins utilisés par les Boutons
Bouton = {
    "bouton_PLAYPAS" : 23,
    "bouton_PLAY" : 18,
    "bouton_PREV" : 15,
    "bouton_NEXT" : 14,
        }

Etat_encodeur = {
    "encodeur_NOTE" : None,
    "encodeur_GATE" : None,
    "encodeur_CV1" : None,
    "encodeur_CV2" : None,
    "encodeur_CV3" : None,
    "encodeur_CV4" : None,
    "encodeur_PARAM" : None
    }
