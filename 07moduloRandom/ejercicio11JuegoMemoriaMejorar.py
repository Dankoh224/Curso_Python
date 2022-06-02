# Juego de memoria. Te muestra cuatro colores de una lista de 10 y te da tres segundos para recordarlos en el orden en el que aparecían. Si aciertas te los vuelve a mostrar en otro orden distinto.
import time
import random
jugar = True
while jugar:
    lista = ["rojo","azul","verde","gris","negro","amarillo","rosa","celeste","cafe","morado"]
    lista = random.sample(lista,4)
    comienzo = str(input('¿Estás listo? Memoriza los colores que aparecerán a continuación. Presiona "ENTER" para continuar:'))
    print(lista)
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
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

    contador = 0
    while contador <= 3:
        contador += 1
        intento = str(input("Ingresa el COLOR {}: ".format(contador)))
        if intento == lista[contador - 1]:
            print("Muy bien.")
        else:
            print("Has perdido. Fin del juego.")
            jugar = False
            break