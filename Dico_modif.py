import threading
from CONFIG_2 import *
from Affichageécran import Display

affichagee = Display()
class Action:
    
    global GEN, SEQ

    def __init__(self, liste_gam, melodie, affichage):
        self.liste_gam = liste_gam
        self.melodie = melodie
        self.affichage = affichage
        self.egg = True

    def param_chang(self):
        GEN["actuel"][1] = (GEN["actuel"][1] + 1) % 3
        #print(GEN)
        affichagee.param('pas'+ str(GEN['actuel'][0]))

    def param_increase(self):
        actuel = GEN["actuel"]
        num_param = actuel[1]
        step = 1
        long_max = 64
        bpm_max = 500
        gam_max = 2

        if num_param == 0:
            if GEN["long"] + step <= long_max:
                GEN["long"] += step
                
                #print(GEN)
                affichagee.param('pas'+ str(GEN['actuel'][0]))
                
        elif num_param == 1:
            if GEN["bpm"] + step <= bpm_max:
                GEN["bpm"] += step
                if GEN["bpm"] == 500 :
                    if self.egg == True :
                        thread = threading.Thread(target=self.melodie.joue_meg)
                        thread.start()
                        self.egg = False
                    
                
                #print(GEN)
                affichagee.param('pas'+ str(GEN['actuel'][0]))
                
        elif num_param == 2:
            if GEN["gamme"] + step <= gam_max:
                GEN["gamme"] += step
                SEQ['pas' + str(GEN['actuel'][0])]['note'] = 'C2'
                #print(GEN)
                affichagee.param('pas'+ str(GEN['actuel'][0]))
                affichagee.note('pas'+ str(GEN['actuel'][0]))
                
    def param_decrease(self):
        actuel = GEN["actuel"]
        num_pas = actuel[0]
        num_param = actuel[1]
        step = 1
        long_min = 1
        bpm_min = 1
        gam_min = 0
        
        if num_param == 0:
            if GEN["long"] - step >= long_min:
                if num_pas <= GEN["long"] - step:
                    GEN["long"] -= step
                    
                    #print(GEN)
                    affichagee.param('pas'+ str(GEN['actuel'][0]))
                    
        elif num_param == 1:
            if GEN["bpm"] - step >= bpm_min:
                GEN["bpm"] -= step
                
                #print(GEN)
                affichagee.param('pas'+ str(GEN['actuel'][0]))
                
        elif num_param == 2:
            if GEN["gamme"] - step >= gam_min:
                GEN["gamme"] -= step
                SEQ['pas' + str(GEN['actuel'][0])]['note'] = 'C2'
                #print(GEN)
                affichagee.param('pas'+ str(GEN['actuel'][0]))
                affichagee.note('pas'+ str(GEN['actuel'][0]))
                
    def note_increase(self):
        actuel = GEN["actuel"]
        gam = self.liste_gam[GEN["gamme"]]

        note_pre = SEQ["pas{}".format(actuel[0])]["note"]
        lettre_pre, chiffre = gam.separation(note_pre)

        lettre_suiv = gam.next_lettre(lettre_pre, '+')

        note_suiv = lettre_suiv + str(chiffre)
        SEQ["pas{}".format(actuel[0])]["note"] = note_suiv
        
        #print(SEQ['pas' + str(GEN['actuel'][0])])
        affichagee.note('pas'+ str(GEN['actuel'][0]))
        
    def note_decrease(self):
        actuel = GEN["actuel"]
        gam = self.liste_gam[GEN["gamme"]]

        note_pre = SEQ["pas{}".format(actuel[0])]["note"]
        lettre_pre, chiffre = gam.separation(note_pre)

        lettre_suiv = gam.next_lettre(lettre_pre, '-')

        note_suiv = lettre_suiv + str(chiffre)
        SEQ["pas{}".format(actuel[0])]["note"] = note_suiv
        
        #print(SEQ['pas' + str(GEN['actuel'][0])])
        affichagee.note('pas'+ str(GEN['actuel'][0]))
        
    def octave(self):
        actuel = GEN["actuel"]
        gam = self.liste_gam[GEN["gamme"]]

        note_pre = SEQ["pas{}".format(actuel[0])]["note"]
        lettre, chiffre_pre = gam.separation(note_pre)

        chiffre_suiv = gam.next_chiffre(chiffre_pre)

        note_suiv = lettre + str(chiffre_suiv)
        SEQ["pas{}".format(actuel[0])]["note"] = note_suiv
        
        #print(SEQ['pas' + str(GEN['actuel'][0])])
        affichagee.note('pas'+ str(GEN['actuel'][0]))
        
    def gate_increase(self):
        actuel = GEN["actuel"]
        step = 0.1
        gate_max = 1

        if round(SEQ["pas{}".format(actuel[0])]["gate"] + step, 2) <= gate_max:
            SEQ["pas{}".format(actuel[0])]["gate"] = round(SEQ["pas{}".format(actuel[0])]["gate"] + step, 2)
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.gate('pas'+ str(GEN['actuel'][0]))
            
    def gate_decrease(self):
        actuel = GEN["actuel"]
        step = 0.1
        gate_min = 0

        if round(SEQ["pas{}".format(actuel[0])]["gate"] - step, 2) >= gate_min:
            SEQ["pas{}".format(actuel[0])]["gate"] = round(SEQ["pas{}".format(actuel[0])]["gate"] - step, 2)
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.gate('pas'+ str(GEN['actuel'][0]))
            
    def silence(self):
        actuel = GEN["actuel"]
        SEQ["pas{}".format(actuel[0])]["gate"] = 0.0
        
        #print(SEQ['pas' + str(GEN['actuel'][0])])
        affichagee.gate('pas'+ str(GEN['actuel'][0]))
        
    def cv1_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv1_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv1"] + step <= cv1_max:
            SEQ["pas{}".format(actuel[0])]["cv1"] += step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv1('pas'+ str(GEN['actuel'][0]))
            
    def cv1_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv1_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv1"] - step >= cv1_min:
            SEQ["pas{}".format(actuel[0])]["cv1"] -= step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv1('pas'+ str(GEN['actuel'][0]))
            
    def cv2_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv2_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv2"] + step <= cv2_max:
            SEQ["pas{}".format(actuel[0])]["cv2"] += step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv2('pas'+ str(GEN['actuel'][0]))
            
    def cv2_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv2_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv2"] - step >= cv2_min:
            SEQ["pas{}".format(actuel[0])]["cv2"] -= step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv2('pas'+ str(GEN['actuel'][0]))
            
    def cv3_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv3_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv3"] + step <= cv3_max:
            SEQ["pas{}".format(actuel[0])]["cv3"] += step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv3('pas'+ str(GEN['actuel'][0]))
            
    def cv3_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv3_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv3"] - step >= cv3_min:
            SEQ["pas{}".format(actuel[0])]["cv3"] -= step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv3('pas'+ str(GEN['actuel'][0]))
            
    def cv4_increase(self):
        actuel = GEN["actuel"]
        step = 5
        cv4_max = 100

        if SEQ["pas{}".format(actuel[0])]["cv4"] + step <= cv4_max:
            SEQ["pas{}".format(actuel[0])]["cv4"] += step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv4('pas'+ str(GEN['actuel'][0]))
            
    def cv4_decrease(self):
        actuel = GEN["actuel"]
        step = 5
        cv4_min = 0

        if SEQ["pas{}".format(actuel[0])]["cv4"] - step >= cv4_min:
            SEQ["pas{}".format(actuel[0])]["cv4"] -= step
            
            #print(SEQ['pas' + str(GEN['actuel'][0])])
            affichagee.cv4('pas'+ str(GEN['actuel'][0]))
            
    def play(self):
        thread = threading.Thread(target=self.melodie.joueSEQ)
        thread.start()

    def playpas(self):
        self.melodie.jouePAS()

    def next(self):
        GEN["actuel"][0] = (GEN["actuel"][0] + 1) % (GEN["long"] + 1)
        if GEN["actuel"][0] == 0:
            GEN["actuel"][0] = 1
        
        #print(GEN['actuel'][0])
        #print(SEQ['pas' + str(GEN['actuel'][0])])
        affichagee.pas('pas'+ str(GEN['actuel'][0]))
        
    def prev(self):
        GEN["actuel"][0] -= 1
        if GEN["actuel"][0] == 0:
            GEN["actuel"][0] = GEN['long']
        
        #print(GEN['actuel'][0])
        #print(SEQ['pas' + str(GEN['actuel'][0])])
        affichagee.pas('pas'+ str(GEN['actuel'][0]))