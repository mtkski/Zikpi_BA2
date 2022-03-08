from Adafruit_GPIO import I2C
tca = I2C.get_i2c_device(address=0x70)
import Adafruit_MCP4725
import time

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
    return valeur_dac
