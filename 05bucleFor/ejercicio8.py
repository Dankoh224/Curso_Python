# Juego que te pide que adivines una letra y te pide letras constantemente hasta que la adivines, luego, para. Se puede probar con todas, menos con la "w". En este caso muestra que esa letra no está permitida y detén el programa.
letra = "m"
while True:
    intento = str(input("Adivina la letra: "))
    if letra == intento:
        print("Adivinaste, la letra era {}.".format(intento))
        break
    if intento == "w":
        print("Se puede probar con todas, menos con la w.")
        break
