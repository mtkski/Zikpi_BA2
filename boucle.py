# Boucle
while True:
  """
  Prise de valeur
  """
    for encoder in encoder_list:
        if encoder.motion_sensor() == "button pressed":
            GEN, SEQ = encoder.dictionary_modification(None, GEN, SEQ)

        elif encoder.motion_sensor() == "rotated clockwise":
            GEN, SEQ = encoder.dictionary_modification("+", GEN, SEQ)

        elif encoder.motion_sensor() == "rotated counter-clockwise":
            GEN, SEQ = encoder.dictionary_modification("-", GEN, SEQ)

    for button in button_list:
        if button.motion_sensor() == "button pressed":
            GEN = button.dictionary_modification(GEN)
