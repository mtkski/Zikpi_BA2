import LCD
from CONFIG_2 import SEQ, GEN
#from Dico_modif import SEQ

class Display:
    def __init__(self):
        self.mylcd = LCD.lcd()

    def all(self,pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)
        
    def note(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string('   ', 1)
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)

    def gate(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string('   ', 2)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)

    def cv1(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string('   ', 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)

    def cv2(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string('   ', 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)

    def cv3(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string('   ', 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)

    def cv4(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string('   ', 2, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)

    def param(self, pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('    ', 1, 12)
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('    ', 1, 12)
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('    ', 1, 12)
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)
            
    def pas(self,pas):
        ICI = SEQ[pas]
        self.mylcd.lcd_clear()
        self.mylcd.lcd_display_string(ICI['note'], 1)
        self.mylcd.lcd_display_string(str(ICI['gate']), 2)
        self.mylcd.lcd_display_string(str(ICI['cv1']), 1, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv2']), 2, 4)
        self.mylcd.lcd_display_string(str(ICI['cv3']), 1, 8)
        self.mylcd.lcd_display_string(str(ICI['cv4']), 2, 8)
        self.mylcd.lcd_display_string('P'+pas[3:5], 2, 12)
        a=GEN['actuel'][1]
        if a==0:
            self.mylcd.lcd_display_string('L' +str(GEN["long"]), 1, 12)
        elif a==1:
            self.mylcd.lcd_display_string('B' +str(GEN["bpm"]), 1, 12)
        elif a==2:
            self.mylcd.lcd_display_string('g' +str(GEN["gamme"]+1), 1, 12)
