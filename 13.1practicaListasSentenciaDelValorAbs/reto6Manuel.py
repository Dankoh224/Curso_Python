# Programa que crea una baraja de 40 cartas, las baraja y las muestra. Luego reparte 5 cartas a 4 jugadores. Muestra las cartas de cada jugador y finalmente muestra las 20 cartas restantes.
import random
numeroCarta = ["1","2","3","4","5","6","7","caballero","reina","rey"]
tipoCarta = ["oro","copa","basto","espada"]
baraja = []
for i in numeroCarta:
    for j in tipoCarta:
        baraja.append("{} de {}.".format(i,j))
mostrarBaraja = []
contador = 0

while contador < len(baraja):
    x = random.randint(0,len(baraja)-1)
    if baraja[x] not in mostrarBaraja:
        mostrarBaraja.append(baraja[x])
        contador += 1
print("Cartas Barajadas:")
print()
print(mostrarBaraja)

jugador1 = []
jugador2 = []
jugador3 = []
jugador4 = []

for i in range(5):
    carta1 = mostrarBaraja.pop(0)
    jugador1.append(carta1)
    carta2 = mostrarBaraja.pop(0)
    jugador2.append(carta2)
    carta3 = mostrarBaraja.pop(0)
    jugador3.append(carta3)
    carta4 = mostrarBaraja.pop(0)
    jugador4.append(carta4)
print()
print("Jugador 1:")
print(jugador1)
print("Jugador 2:")
print(jugador2)
print("Jugador 3:")
print(jugador3)
print("Jugador 4:")
print(jugador4)
print()
print("El resto de cartas es:")
print(mostrarBaraja)