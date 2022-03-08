from Adafruit_GPIO import I2C
tca = I2C.get_i2c_device(address=0x70)
import Adafruit_MCP4725
import time
from Fonctions_envoi_valeur import tca_set, bpm_to_s

dac = Adafruit_MCP4725.MCP4725(address=0x60)

SEQ = {}
for i in range(1,9):
    PARAM = {"note":2048, "gate":1, "cv1":2048, "cv2":0, "cv3":0, "cv4":0}
    SEQ["pas"+str(i)] = PARAM

SEQ['pas1']['gate'] = 0

SEQ['pas1']['cv1'] = 200
SEQ['pas2']['cv1'] = 500
SEQ['pas3']['cv1'] = 900
SEQ['pas4']['cv1'] = 1000
SEQ['pas5']['cv1'] = 2000
SEQ['pas6']['cv1'] = 2800
SEQ['pas7']['cv1'] = 3400
SEQ['pas8']['cv1'] = 4096

SEQ['pas1']['note'] = int(4096/5)
SEQ['pas2']['note'] = 0
SEQ['pas3']['note'] = int(4096/4)
SEQ['pas4']['note'] = 0
SEQ['pas5']['note'] = int(4096/3)
SEQ['pas6']['note'] = 0
SEQ['pas7']['note'] = int(4096/2)
SEQ['pas8']['note'] = 0

#print(SEQ)
duree_pas = bpm_to_s(int(60))
#print(duree_pas)
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
while True :
    for i in range(1,9) : #play
        tca_set(0b00001000)                       # cv1
        dac.set_voltage(SEQ['pas'+ str(i) ]['cv1'])
        #print(SEQ['pas'+ str(i) ]['cv1']   )
        #print(SEQ['pas'+ str(i) ]['cv1'])
        """

        tca_set(0b00000000)                       # cv2
        dac.set_voltage(SEQ['pas' + str(i)]['cv2'])
        
        tca_set(0b00000000)                       # cv3
        dac.set_voltage(SEQ['pas' + str(i)]['cv3'])

        tca_set(0b00000000)                       # cv4
        dac.set_voltage(SEQ['pas' + str(i)]['cv4'])
        """
        
        
        tca_set(0b00000010)                       # gate
        dac.set_voltage(4096)
        #print('volt set')
        time.sleep(SEQ['pas' + str(i)]['gate'] * duree_pas)
        dac.set_voltage(0)
        #print('volt 0')
        time.sleep(duree_pas - SEQ['pas' + str(i)]['gate'] * duree_pas )
        
        tca_set(0b00000001)                       # note
        dac.set_voltage(SEQ['pas' + str(i)]['note'])
        print(SEQ['pas'+ str(i) ]['note'])
        
tca_set(0b00000010)
dac.set_voltage(0)
#test bnidon
#dfgeg
