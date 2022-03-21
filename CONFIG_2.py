from gpiozero import Button
from gpiozero import RotaryEncoder
import RPi.GPIO as GPIO

max = 64
SEQ = {}
for i in range(1,max+1):
    PARAM = {"note":'C2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM

# SEQ['pas1']['note'] = 1 pour modifier (exemple)
# actuel = [num du pas, numéro du paramètre de l'encodeur PARAM (0:long, 1:bpm, 2:gamme)]

GEN = {"long":8, "bpm":498, "gamme":0, "actuel" : [1,0]}

GEN_DE = {"long":16, "bpm":238, "gamme":0, "actuel" : [1,0]}

SEQ_DE = {
'pas1' : {"note":'A2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas2' : {"note":'A2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas3' : {"note":'A1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas4' : {"note":'A1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas5' : {"note":'E2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas6' : {"note":'E2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas7' : {"note":'A1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas8' : {"note":'A1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas9' : {"note":'A2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas10' : {"note":'A2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas11' : {"note":'F2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas12' : {"note":'A1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas13' : {"note":'G2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas14' : {"note":'G2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas15' : {"note":'G1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas16' : {"note":'G1', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
}

GEN_mega = {"long":32, "bpm":500, "gamme":0, "actuel" : [1,0]}

megalovania = {
'pas1' : {"note":'D2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas2' : {"note":'D2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas3' : {"note":'D3', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas4' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas5' : {"note":'A2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas6' : {"note":'E2', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas7' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas8' : {"note":'G#2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas9' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas10' : {"note":'G2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas11' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas12' : {"note":'F2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas13' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas14' : {"note":'D2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas15' : {"note":'F2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas16' : {"note":'G2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas17' : {"note":'C2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas18' : {"note":'C2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas19' : {"note":'D3', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas20' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas21' : {"note":'A2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas22' : {"note":'E2', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas23' : {"note":'A1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas24' : {"note":'G#2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas25' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas26' : {"note":'G2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas27' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas28' : {"note":'F2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas29' : {"note":'C1', "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas30' : {"note":'D2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas31' : {"note":'F2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0},
'pas32' : {"note":'G2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
}

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

    