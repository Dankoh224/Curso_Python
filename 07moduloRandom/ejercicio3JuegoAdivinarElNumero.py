# Juego que genera un número aleatorio del 1 al 100 y te pide que lo adivines. Se te va indicando si el número que introduces es mayor o menor que el que hay que adivinar. Tienes 7 intentos, si no, el programa se termina y te dice que has perdido.
import random
numero = random.randint(1,100)
for i in range(7):
    if i >= 6:
        intento = int(input("Es tu último intento. Adivina el número: "))
        if intento == numero:
            print("¡Adivinaste! El número {} es el valor a encontrar ¡GANASTE!".format(intento))
            break
        else:
            print("No has acertado. Perdiste")
    else:
        intento = int(input("Adivina el número: "))
        if intento == numero:
            print("¡Adivinaste! El número {} es el valor a encontrar ¡GANASTE!".format(intento))
            break
        else:
            if i != 5:
                if numero < intento:
                    print("No has acertado. El número que debes adivinar es MENOR al ingresado. Vuelve a intentarlo, te quedan: {} intentos.".format(6-i))
                elif numero > intento:
                    print("No has acertado. El número que debes adivinar es MAYOR al ingresado. Vuelve a intentarlo, te quedan: {} intentos.".format(6-i))
            else:
                if numero < intento:
                    print("No has acertado. El número que debes adivinar es MENOR al ingresado. Vuelve a intentarlo, te queda: {} intento.".format(6-i))
                elif numero > intento:
                    print("No has acertado. El número que debes adivinar es MAYOR al ingresado. Vuelve a intentarlo, te queda: {} intento.".format(6-i))