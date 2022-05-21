# Juego que genera un número aleatorio del 1 al 100 y te pide que lo adivines. Se te va indicando si el número que introduces es mayor o menor que el que hay que adivinar. Tienes 7 intentos, si no, el programa se termina y te dice que has perdido.
import random
numero = random.randint(1,100)
contador = 0
jugar = True
while jugar:
    contador += 1
    if contador <= 7:
        intento = int(input("Ingresa número: "))
        if numero > intento:
            print("El número a adivinar es mayor que el que ingresaste. Te queda {} intento.".format((7 - contador)))
        elif numero < intento:
            print("El número a adivinar es menor que el que ingresaste. Te queda {} intento.".format((7 - contador)))
        else:
            print("Ganaste. El número es el {}".format(intento))
            break
    else:
        print("Has perdido")
        jugar = False