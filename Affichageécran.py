import time
import LCD
from CONFIG import SEQ

def affichervaleurs(pas):
    ICI=SEQ[pas]
    mylcd =LCD.lcd()
    mylcd.lcd_display_string(ICI['note'],1)
    mylcd.lcd_display_string(str(ICI['gate']),2)
    mylcd.lcd_display_string(str(ICI['cv1']),1,4)
    mylcd.lcd_display_string(str(ICI['cv2']),2,4)
    mylcd.lcd_display_string(str(ICI['cv3']),1,8)
    mylcd.lcd_display_string(str(ICI['cv4']),2,8)
    mylcd.lcd_display_string('PARA',1,12)
    mylcd.lcd_display_string('VALE',2,12)
