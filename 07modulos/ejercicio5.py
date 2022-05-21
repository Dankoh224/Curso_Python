# Programa que simula 100 tiradas de una moneda y comprueba cuántas veces sale cada resultado posible.
import random
lista = ["cara","sello"]
contadorCara = 0
contadorSello = 0
for i in range (100):
    lanzamientoMoneda = random.choice(lista)
    print(lanzamientoMoneda)
    if lanzamientoMoneda == "cara":
        contadorCara += 1
    else:
        contadorSello += 1
print("La cantidad de veces que salió cara es de {} y la cantidad de veces que salió sello es de {}.".format(contadorCara,contadorSello))
