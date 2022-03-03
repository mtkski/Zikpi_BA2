# IN : numéro de la note [1,60]
# Prend le numéro de la note et lui associe un voltage qui va de 1 à 5
# OUT : nom de la note associé au numéro de la note

def Note(num_note):
    Lettre_note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    octave = int((num_note*5)/60 + 0.99)
    lettre = num_note % 12

    return Lettre_note[lettre - 1] + str(octave)



for i in range(1,61,1) :
    print(Note(i))
