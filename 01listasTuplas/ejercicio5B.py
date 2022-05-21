# Programa que pide que tres jugadores introduzcan un número y espera a que los tres jugadores hayan introducido el número.
inicio = True
jugadorA = None
jugadorB = None
jugadorC = None
while inicio:
    print("Pulsa:")
    print("1. Para jugador A")
    print("2. Para jugador B")
    print("3. Para jugador C")
    print()
    jugador = int(input("Ingrese una opción: "))
    if jugador in [1,2,3]:
        while jugador == 1:
            if jugadorA == None:
                jugadorA = int(input("Ingrese número: "))
                break
            else:
                jugador = int(input("El jugador 1 ya tiene asignado un valor.Ingrese una opción: "))
        while jugador == 2:
            if jugadorB == None:
                jugadorB = int(input("Ingrese número: "))
                break
            else:
                jugador = int(input("El jugador 2 ya tiene asignado un valor.Ingrese una opción: "))  
        while jugador == 3:
            if jugadorC == None:
                jugadorC = int(input("Ingrese número: "))
                break
            else:
                jugador = int(input("El jugador 3 ya tiene asignado un valor.Ingrese una opción: "))
        if jugadorA is not None and jugadorB is not None and jugadorC is not None:
            print("Los tres jugadores ya han elegido número:")
            print("Jugador A: {}".format(jugadorA))
            print("Jugador B: {}".format(jugadorB))
            print("Jugador C: {}".format(jugadorC))
            inicio = False
    else:
        print("La opción es inválida. Vuelva a intentar.")