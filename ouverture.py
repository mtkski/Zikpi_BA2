import LCD
from time import *
from envoi_valeurs import Melody

mylcd = LCD.lcd()

def démarrage() :
    mylcd.lcd_display_string("Demarrage", 1, 3)
    
    for i in range(17):
        mylcd.lcd_display_string('.',2,i)
        sleep(0.05)
        
    melodie_dem = Melody()
    melodie_dem.joue_dem()

    sleep(0.3)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("ZIKPI", 1, 5)
    mylcd.lcd_display_string("Direct tu die", 2, 1)
    sleep(2)