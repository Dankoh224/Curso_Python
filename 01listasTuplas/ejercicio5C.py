# Programa que pide que tres jugadores introduzcan un número y espera a que los tres jugadores hayan introducido el número.
jugadorA = jugadorB = jugadorC = None
while jugadorA is None or jugadorB is None or jugadorC is None:
    print("Pulsa: \n 1. Para jugador A \n 2. Para jugador B \n 3. Para jugador C \n")
    jugador = int(input("Ingrese opcion: "))
    if jugador == 1 and jugadorA is None:
        jugadorA = int(input("Ingrese número: "))
    elif jugador == 2 and jugadorB is None:
        jugadorB = int(input("Ingrese número: "))
    elif jugador == 3 and jugadorC is None:
        jugadorC = int(input("Ingrese número: "))
    else:
        print("La opción ingresada no es válida.")
print("\n Jugador 1: {} \n Jugador 2: {} \n Jugador 3: {}".format(jugadorA,jugadorB,jugadorC))