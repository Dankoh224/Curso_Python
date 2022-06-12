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
contador = 0
while contador < 5:
    x = random.randint(0,len(baraja)-1)
    if mostrarBaraja[x] not in jugador1 and mostrarBaraja[x] not in jugador2 and mostrarBaraja[x] not in jugador3 and mostrarBaraja[x] not in jugador4:
        jugador1.append(mostrarBaraja[x])
        contador += 1
print()
print("Las cartas del jugador 1 son:")
print(jugador1)

contador = 0
while contador < 5:
    x = random.randint(0,len(baraja)-1)
    if mostrarBaraja[x] not in jugador1 and mostrarBaraja[x] not in jugador2 and mostrarBaraja[x] not in jugador3 and mostrarBaraja[x] not in jugador4:
        jugador2.append(mostrarBaraja[x])
        contador += 1
print("Las cartas del jugador 2 son:")
print(jugador2)

contador = 0
while contador < 5:
    x = random.randint(0,len(baraja)-1)
    if mostrarBaraja[x] not in jugador1 and mostrarBaraja[x] not in jugador2 and mostrarBaraja[x] not in jugador3 and mostrarBaraja[x] not in jugador4:
        jugador3.append(mostrarBaraja[x])
        contador += 1
print("Las cartas del jugador 3 son:")
print(jugador3)

contador = 0
while contador < 5:
    x = random.randint(0,len(baraja)-1)
    if mostrarBaraja[x] not in jugador1 and mostrarBaraja[x] not in jugador2 and mostrarBaraja[x] not in jugador3 and mostrarBaraja[x] not in jugador4:
        jugador4.append(mostrarBaraja[x])
        contador += 1
print("Las cartas del jugador 4 son:")
print(jugador4)
print()

copiaMostrarBaraja = list(mostrarBaraja)
for i in copiaMostrarBaraja:
    if i in jugador1 or i in jugador2 or i in jugador3 or i in jugador4:
        mostrarBaraja.remove(i)

print()
print("Las cartas que quedan después del reparto son:")
print()
print(mostrarBaraja)
