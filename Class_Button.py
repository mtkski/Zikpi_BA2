# Classe définissant les boutons
class Button:

    # IN : le nom du bouton et le numéro de la pin
    # Définit l'objet button, PreValue est une valeur utile pour la méthode "motion_sensor"
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.PreValue = GPIO.input(pin)

    # Détecte les actions sur les boutons (utilisation du bouton poussoir)
    def motion_sensor(self):
        buttonvalue = GPIO.input(self.pin)

        if buttonvalue != self.PreValue:
            while not buttonvalue == 0:
                buttonvalue = GPIO.input(self.pin)
            return "button pressed"

    # IN : le dictionnaires de valeur GEN (voir CONFIG.py)
    # Modifie la valeurs "actuel" dans le dictionnaires de valeur GEN
    def dictionary_modification(self, gen):
        pas_max = gen["long"]

        if self.name == "bouton_PREV":
            if gen["actuel"][0] < pas_max:
                gen["actuel"][0] += 1

        elif self.name == "bouton_NEXT":
            if gen["actuel"][0] > 0:
                gen["actuel"][0] -= 1
        sleep(0.2)
        return gen
