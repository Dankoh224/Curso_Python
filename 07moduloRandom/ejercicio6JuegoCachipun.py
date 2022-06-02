# Programar un cachipún.
import random
opciones = ["piedra","papel","tijera"]
puntaje = 0
puntajeMaquina = 0
juego = 0
for i in range(10):
    cachipun = random.choice(opciones)
    juego += 1
    intento = str(input("Juego nº {}. Ingresa tu apuesta: ".format(juego)))
    print("La máquina eligió {}.".format(cachipun))
    if intento == cachipun:
        print("Es un empate.")
    else:
        if cachipun == "piedra" and intento == "tijera":
            puntajeMaquina += 1
            print("Has perdido.")
        elif cachipun == "piedra" and intento == "papel":
            puntaje += 1
            print("Has ganado.")
        
        elif cachipun == "papel" and intento == "tijera":
            puntaje += 1
            print("Has ganado.")
        elif cachipun == "papel" and intento == "piedra":
            puntajeMaquina += 1
            print("Has perdido.")

        elif cachipun == "tijera" and intento == "papel":
            puntajeMaquina += 1
            print("Has perdido.")
        elif cachipun == "tijera" and intento == "piedra":
            puntaje += 1
            print("Has ganado.")
print("Tu puntaje es de {} puntos y el de la maquina es de {}.".format(puntaje,puntajeMaquina))
if puntajeMaquina>puntaje:
    print("¡You Lose!")
elif puntaje == puntajeMaquina:
    print("¡Es un empate!")
else:
    print("¡You Win!")