max = 64
SEQ = {}
for i in range(1,max+1):
    PARAM = {"note":'C2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM

# SEQ['pas1']['note'] = 1 pour modifier (exemple)
# actuel = [num du pas, numéro du paramètre de l'encodeur PARAM (1:long, 2:bpm, 3:gamme)]

GEN = {"long":8, "bpm":120, "gamme":1, "actuel" : [1,1]}

bouton_play = Button(18)
bouton_playpas = Button(23)
bouton_next = Button(14)
bouton_prev = Button(15)

encodeur_NOTE = RotaryEncoder(10,9)
encodeur_GATE = RotaryEncoder(5,6)
encodeur_CV1 = RotaryEncoder(20,21)
encodeur_CV2 = RotaryEncoder(12,16)
encodeur_CV3 = RotaryEncoder(8,7)
encodeur_CV4 = RotaryEncoder(24,25)
encodeur_PARAM = RotaryEncoder(13,19)

bouton_NOTE = Button(11)
bouton_GATE = Button(22)
bouton_PARAM = Button(26)
