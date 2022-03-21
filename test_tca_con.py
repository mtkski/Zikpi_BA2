from Adafruit_GPIO import I2C
import Adafruit_MCP4725
import time
from Class_Note import Note
#from CONFIG_2 import GEN_DE, SEQ_DE, megalovania, GEN_mega

dac = Adafruit_MCP4725.MCP4725(address=0x60)
tca = I2C.get_i2c_device(address=0x70)

max = 8
SEQ = {}
for i in range(1,max+1):
    PARAM = {"note":'C2', "gate":0.5, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM
print(SEQ)

GEN = {"long":8, "bpm":120, "gamme":0, "actuel" : [1,0]}

def tca_set(mask):
    """Select one or more channels.
           chan =   76543210
           mask = 0b00000000
    """
    if mask > 0xff:
        return
    tca.writeRaw8(mask)
    
    
def bpm_to_s(bpm):
    s = (60 / bpm) 
    return s

def pourcent_to_DAC(pourcent) :
    valeur_dac = (4096/100) * pourcent
    return int(valeur_dac)

def traduction_note_to_DACfct(symbole):
        dico_note = {}
        
        for i in range(1,61,1):
            Lettre_note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
            octave = int((i) / 12 + 0.99)
            lettre = i % 12
            valeur_dac = i * (4096/59)
            dico_note[Lettre_note[lettre - 1] + str(octave)] = valeur_dac - (4096/59)

        return int(dico_note.get(symbole))
    
"""    
def joueSEQ():
        duree_pas = bpm_to_s(int(GEN['bpm']))
        play = True
        while play == True :
            for i in range(1,GEN['long']+1) : #play
                if play == True:
                    tca_set(0b00001000)                       # cv1
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas'+ str(i) ]['cv1']))
                    print('a')
                if play == True:
                    tca_set(0b00000100)                       # cv2
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(i)]['cv2']))
                print('b')
                if play == True:
                    tca_set(0b00010000)                       # cv3
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(i)]['cv3']))
                
                if play == True:
                    tca_set(0b00100000)                       # cv4
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(i)]['cv4']))
                
                if play == True:
                    tca_set(0b00000010)                       # note
                    dac.set_voltage(traduction_note_to_DACfct(SEQ['pas' + str(i)]['note']))
                
                if play == True:
                    tca_set(0b00000001)                       # gate
                    dac.set_voltage(4096)
                    time.sleep(SEQ['pas' + str(i)]['gate'] * duree_pas)
                    dac.set_voltage(0)
                    time.sleep(duree_pas - (SEQ['pas' + str(i)]['gate'] * duree_pas))
"""                    
                    
                    
#joueSEQ()
"""
for i in range(2) :
    tca_set(0b11111111)
    dac.set_voltage(2048)
    print('1')

    time.sleep(2)

    tca_set(0b11111111)
    dac.set_voltage(1)
    print('2')

    time.sleep(2)

    tca_set(0b11111111)
    dac.set_voltage(3048)
    print('3')
    
    time.sleep(2)
"""
"""
tca_set(0b00000010)
dac.set_voltage(2000)
"""
while True :
    tca_set(0b00000010)
    dac.set_voltage(1)
    time.sleep(1)
    
    
    tca_set(0b00000010)
    dac.set_voltage(2000)
    time.sleep(1)
    print('ye')
