# Programa que pide que tres jugadores introduzcan un número y espera a que los tres jugadores hayan introducido el número.
print("Pulsa:")
print("1. Para jugador A")
print("2. Para jugador B")
print("3. Para jugador C")
print()
jugador = None
A = 0
B = 0
C = 0
inicio = True
while inicio:
    jugador = int(input("Elige jugador: "))
    if jugador == 1 or jugador == 2 or jugador == 3:
        while jugador == 1 or jugador == 2 or jugador == 3:
            numero = int(input("Ingresa un número: "))
            if jugador == 1:
                a = numero
                A = None
            if jugador == 2:
                b = numero
                B = None
            if jugador == 3:
                c = numero
                C = None
            if A is None and B is None and C is None:
                break
            jugador = int(input("Elige jugador: "))
            while True:
                if jugador == 1 and A is None:
                    print("El jugador 1 ya ha elegido.")
                    jugador = int(input("Elige jugador: "))
                elif jugador == 2 and B is None:
                    print("El jugador 2 ya ha elegido.")
                    jugador = int(input("Elige jugador: "))
                elif jugador == 3 and C is None:
                    print("El jugador 3 ya ha elegido.")
                    jugador = int(input("Elige jugador: "))
                else:
                    break
        print("Los tres jugadores ya han elegido número:")
        print("Jugador A: {}".format(a))
        print("Jugador B: {}".format(b))
        print("Jugador C: {}".format(c))
        inicio = False
    else:
        print("Error de opción.")



