# Programa que pide que tres jugadores introduzcan un número y espera a que los tres jugadores hayan introducido el número.
opcion = None
jugador1 = None
jugador2 = None
jugador3 = None

while jugador1 is None or jugador2 is None or jugador3 is None: 
    print("A continuación se presentan tres opciones:")
    print("\n1) Jugador A.")
    print("2) Jugador B.")
    print("3) Jugador C.")
    opcion = int(input("\nIngrese el número del jugador que usted desea: "))
    if opcion == 1 and jugador1 is None:
        jugador1 = int(input("Asigna un valor para este jugador: "))
    elif opcion == 2 and jugador2 is None:
        jugador2 = int(input("Asigna un valor para este jugador: "))
    elif opcion == 3 and jugador3 is None:
        jugador3 = int(input("Asigna un valor para este jugador: "))
    else:
        if opcion == 1:
            print("\nAl jugador 1 ya se le ha asignado un valor.\n")
        if opcion == 2:
            print("\nAl jugador 2 ya se le ha asignado un valor.\n")
        if opcion == 3:
            print("\nAl jugador 3 ya se le ha asignado un valor.\n")
        if opcion > 3 or opcion < 1:
            print("\nLa opción elegida no es válida. Vuelva a intentar.\n")
print("\n¡Excelente! Ya has ingresado los valores para todos los jugadores:")
print("Jugador 1: {}.".format(jugador1))
print("Jugador 2: {}.".format(jugador2))
print("Jugador 3: {}.".format(jugador3))
print("\nFin del programa")