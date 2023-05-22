# La ciudad se ha llenado de zombies. Estás en la calle 1 y has de llegar a la calle 40 para poder salvarte.
# Los zombies avanzan 1, 2, y 3 calles. Tu puedes avanzar 1, 2, y 3 calles.
# ¿Estás preparado, ¿cuál es tu nombre?
# El juego debe decir:
# Estás en la calle 1. Hay zonmbies en las calles 10, 12, 12, 14, 15, 16, 16, 17, 19 y 20.
# ¿Cuánto quieres correr? (1,2,3):
from persona import Persona
from zombie import Zombie
import os

os.system('cls')

print('La ciudad se ha llenado de zombies. Estás en la calle 1 y has de llegar a la calle 40 para poder salvarte.')
print('Los zombies avanzan 1, 2, y 3 calles. Tu puedes avanzar 1, 2, y 3 calles.')

# OBJETO JUGADOR
nombre = str(input('¿Estás preparado, ¿cuál es tu nombre?: '))
jugador = Persona(nombre)


# OBJETO HORDA DE ZOMBIES
horda = []
for i in range(10):
    z = Zombie()
    horda.append(z)

# INICIO DEL JUEGO
while True:
    os.system('cls')

    print()
    print(jugador.situacion())
    print()

    calles = []
    for zombi in horda:
            calles.append(zombi.calle)
    calles.sort()

    print('Hay zombies en las calles: ')
    print()
    print(' ', end = '')
    for elemento in calles:
        print(elemento, end = ' ')
    print()
    print()
    

    if jugador.calle > 40:
        print('No te ha visto ningún zombie.')
        print('No te han comido.')
        print()
        break
    
    comido = False

    for zombi in horda:
        if zombi.calle == jugador.calle:
            comido = True

    if comido:
        print('Te ha visto un zombie.')
        print('Te han comido.')
        print()
        break

    velocidad = ''
    while velocidad not in ('1','2','3'):
        velocidad = str(input('¿Cuánto quieres correr? (1,2,3): '))
    jugador.moverse(velocidad)

    for z in list(horda):
        z.moverse()
        if z.no_visible():
            horda.remove(z)


