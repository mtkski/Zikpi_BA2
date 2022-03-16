import LCD
from CONFIG import SEQ


class Display:

    def all(self,pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(ICI['note'], 1)
        mylcd.lcd_display_string(str(ICI['gate']), 2)
        mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        mylcd.lcd_display_string('PARA', 1, 12)
        mylcd.lcd_display_string('VALE', 2, 12)

    def note(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(ICI['note'], 1)

    def gate(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(str(ICI['gate']),2)

    def cv1(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(str(ICI['cv1']),1,4)

    def cv2(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(str(ICI['cv2']),2,4)

    def cv3(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(str(ICI['cv3']),1,8)

    def cv4(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string(str(ICI['cv4']),2,8)

    def param(self, pas):
        ICI = SEQ[pas]
        mylcd = LCD.lcd()
        mylcd.lcd_display_string('PARA',1,12)
        mylcd.lcd_display_string('VALE',2,12)
