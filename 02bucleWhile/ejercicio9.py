# Juego que pregunte un número del 1 al 15 y luego una vocal. Tienes 100 puntos, si aciertas uno de ellos te quita dos puntos, si no aciertas ninguno te quita 5 puntos. El programa no se acaba hasta que aciertas los dos. Cuando se acaba el programa te dice los puntos que te quedan.
numero = 12
vocal = "i"
ingreso = True
puntos = 100
while ingreso:
    numeroInt = int(input("Ingresa un número del 1 a 15: "))
    vocalInt = str(input("Ingrese una vocal: "))
    if numeroInt == numero and vocalInt == vocal:
        print("¡Excelente, acertaste! Tu puntaje final es de {} puntos.".format(puntos))
        ingreso = False
    elif numeroInt == numero or vocalInt == vocal:
        puntos = puntos - 2
        print("Solo acertaste a uno. Se te descuentan 2 puntos. Tu puntaje ahora es de {} puntos.".format(puntos))
    else:
        puntos = puntos - 5
        print("No acertaste ninguno. Se te descuentan 5 puntos. Tu puntaje ahora es de {} puntos.".format(puntos))