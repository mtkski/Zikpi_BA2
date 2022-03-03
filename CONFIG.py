
max = 64
SEQ = {}
for i in range(1,max+1):
    PARAM = {"note":0, "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM

# SEQ['pas1']['note'] = 1 pour modifier (exemple)
# actuel = [num du pas, numéro du paramètre de l'encodeur PARAM (1:long, 2:bpm, 3:gamme)]

GEN = {"long":0, "bpm":0, "gamme":0, "actuel" : [1,1]}


# pins et autres (adapter avec le produit de philippe)

# Définit les pins utilisés par les encodeurs
Encodeur = {
    "encodeur_NOTE" : [5,6,None],
    "encodeur_GATE" : [9,11,None],
    "encodeur_CV1" : [20,21,None],
    "encodeur_CV2" : [12,16,None],
    "encodeur_CV3" : [8,7,None],
    "encodeur_CV4" : [24,25,None],
    "encodeur_PARAM" : [13,19,26]
    }

# Définit les valeurs initiales des encodeurs
val = [0,0,0,0,0,0,0]

# Définit les paliers en fonction des encodeurs
step = [int(4096/(12*5)),1,1,1,1,1,1]

# pDéfinit l'intervalle des encodeurs
interval = [(0,4096),(0,1),(0,4096),(0,4096),(0,4096),(0,4096),(0,4096)]

# Définit les pins utilisés par les Boutons
Bouton = {
    "bouton_PLAYPAS" : 23,
    "bouton_PLAY" : 18,
    "bouton_PREV" : 15,
    "bouton_NEXT" : 14,
        }
