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


def bpm_to_ms(bpm):
    ms = (60 / bpm) * 1000
    return int(ms)

dac = Adafruit_MCP4725.MCP4725(address=0x60)

SEQ = {}
for i in range(1,9):
    PARAM = {"note":0, "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM
print(SEQ)


duree_pas = bpm_to_ms(int(60))

""""when playpas is pressed
tca_set(0b0000100)                       # cv1
    dac.set_voltage(SEQ['pas'+ i ]['cv1'])

    tca_set(0b0001000)                       # cv2
    dac.set_voltage(SEQ['pas' + i]['cv2'])

    tca_set(0b0010000)                       # cv3
    dac.set_voltage(SEQ['pas' + i]['cv3'])

    tca_set(0b0100000)                       # cv4
    dac.set_voltage(SEQ['pas' + i]['cv4'])

    tca_set(0b0100000)                       # note
    dac.set_voltage(SEQ['pas' + i]['note'])

    tca_set(0b0100000)                       # gate
    dac.set_voltage(4096)
    time.sleep(SEQ['pas' + i]['gate'] * duree_pas)
    dac.set_voltage(0)
"""
#for play press
for i in range(1,9) : #play
    tca_set(0b0000100)                       # cv1
    dac.set_voltage(SEQ['pas'+ i ]['cv1'])

    tca_set(0b0001000)                       # cv2
    dac.set_voltage(SEQ['pas' + i]['cv2'])

    tca_set(0b0010000)                       # cv3
    dac.set_voltage(SEQ['pas' + i]['cv3'])

    tca_set(0b0100000)                       # cv4
    dac.set_voltage(SEQ['pas' + i]['cv4'])

    tca_set(0b0100000)                       # note
    dac.set_voltage(SEQ['pas' + i]['note'])

    tca_set(0b0100000)                       # gate
    dac.set_voltage(4096)
    time.sleep(SEQ['pas' + i]['gate'] * duree_pas)
    dac.set_voltage(0)

    time.sleep(duree_pas - SEQ['pas' + i]['gate'] * duree_pas )