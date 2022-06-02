# Juego idéntico al 3, con la diferencia de decir distintas frases al indicar si el número es demasiado alto o muy bajo.
import random
numero = random.randint(1,100)
juego = 0
jugar = True
while jugar:
    juego += 1
    if juego <= 7:
        intento = int(input("Ingrese un número: "))
        if numero > intento:
            print("El número a adivinar es {}. Llevas {} intento.".format(random.choice(["más grande","mayor","más alto","superior"]),juego))
        elif numero < intento:
            print("El número a adivinar es {}. LLevas {} intento.".format(random.choice(["menor","más pequeño","más bajo","inferior"]),juego))
        else:
            print("Ganaste. El número ganador era el {}.".format(intento))
            break
    else:
        print("Has perdido")
        jugar = False