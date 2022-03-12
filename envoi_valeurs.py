from Adafruit_GPIO import I2C
tca = I2C.get_i2c_device(address=0x70)
import Adafruit_MCP4725
import time
from Class_Note import Note
from CONFIG import *
dac = Adafruit_MCP4725.MCP4725(address=0x60)

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


#print(SEQ)
duree_pas = bpm_to_s(int(GEN['bpm']))
#print(duree_pas)




class Melody :
    
    def __init__(self):
        self.play = False

    def joueSEQ(self):
        global duree_pas
    
        if self.play == True :
            self.play = False
        elif self.play == False :
            self.play = True
    
        while self.play == True :
            for i in range(1,GEN['long']+1) : #play
                if self.play == True:
                    tca_set(0b0000100)                       # cv1
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas'+ str(i) ]['cv1']))
                
                if self.play == True:
                    tca_set(0b0001000)                       # cv2
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(i)]['cv2']))
                
                if self.play == True:
                    tca_set(0b0010000)                       # cv3
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(i)]['cv3']))
                
                if self.play == True:
                    tca_set(0b0100000)                       # cv4
                    dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(i)]['cv4']))
                
                if self.play == True:
                    tca_set(0b0000001)                       # note
                    dac.set_voltage(traduction_note_to_DACfct(SEQ['pas' + str(i)]['note']))
                
                if self.play == True:
                    tca_set(0b0000010)                       # gate
                    dac.set_voltage(4096)
                    time.sleep(SEQ['pas' + str(i)]['gate'] * duree_pas)
                    dac.set_voltage(0)
                    time.sleep(duree_pas - (SEQ['pas' + str(i)]['gate'] * duree_pas))
    def jouePAS(self) :
        pas = GEN['actuel'][0]
        tca_set(0b0000100)                       # cv1
        dac.set_voltage(pourcent_to_DAC(SEQ['pas'+ str(pas) ]['cv1']))

        tca_set(0b0001000)                       # cv2
        dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(pas)]['cv2']))

        tca_set(0b0010000)                       # cv3
        dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(pas)]['cv3']))

        tca_set(0b0100000)                       # cv4
        dac.set_voltage(pourcent_to_DAC(SEQ['pas' + str(pas)]['cv4']))

        tca_set(0b0000001)                       # note
        dac.set_voltage(traduction_note_to_DACfct(SEQ['pas' + str(pas)]['note']))

        tca_set(0b0000010)                       # gate
        dac.set_voltage(4096)
        time.sleep(SEQ['pas' + str(pas)]['gate'] * duree_pas)
        dac.set_voltage(0)
