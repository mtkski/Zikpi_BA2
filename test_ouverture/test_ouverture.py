import LCD
from time import *

mylcd = LCD.lcd()

mylcd.lcd_display_string("Demarrage...", 1, 1)

chargem = [
    [0b11111,
     0b11111,
     0b11111,
     0b11111,
     0b11111,
     0b11111,
     0b11111,
     0b11111],
]

for i in range(16):
    sleep(0.4)
    mylcd.lcd_load_custom_chars(chargem)
    mylcd.lcd_write(0xC0)
    mylcd.lcd_write_char(i)

sleep(0.5)
mylcd.lcd_clear()
mylcd.lcd_display_string("Bienvenue", 1, 1)
