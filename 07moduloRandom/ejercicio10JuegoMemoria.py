# Juego de memoria. Te muestra cuatro colores y te da tres segundos para recordarlos en el orden en el que aparecían. Si aciertas te los vuelve a mostrar en otro orden distinto.
import random
import time
jugar = True
puntaje = 0
segundos = 3
puntajeMayor = 0
while jugar:
    lista = ["rojo","verde","azul","amarillo"]
    lista = random.sample(lista,4)
    print(lista)
    inicio = time.time()
    while True:
        final = time.time()
        if final - inicio >= segundos:
            break
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")
    print("")
    print("Puntaje Mayor: {}".format(puntajeMayor))

    contador = 0
    for i in lista:
        contador += 1
        intento = str(input("¿Cuál es el color número {} de la lista?: ".format(contador)))
        if i == intento:
            print("Bien. continúa.")
            puntaje += 100
        else:
            print("Has perdido, los siento. Obtuviste {} puntos.".format(puntaje))
            jugar = False
            break
    segundos -= 0.5
    
    if puntaje > puntajeMayor:
        puntajeMayor = puntaje

