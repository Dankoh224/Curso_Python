# MUERTOS Y HERIDOS (MASTERMIND)

# 1. Presentación. Usuario tiene que adivinar número antes de 15 intentos.
# 2. Generar un número aleatorio de 4 dígitos (que han de ser distintos).
# 3. Pedir un número de 4 dígitos al usuario (han de ser distintos también).
# 4. Comparar el número del usuario con el generado por el ordenador:
# Por cada dígito que coincide en valor y posición, muertos aumenta 1.
# Por cada dígito que coindice sólo en valor, heridos aumenta 1.
# 5. Mostrar el número de muertos y heridos conseguidos por el usuario.
# 6. Seguir pidiendo números al usuario.
# 7. Mostrar siempre todos los números y resultados dichos hasta el momento.
# 8. Si el usuario acierta los 4 números mostrar que ha ganado y finalizar.
# 9. Más de 15 intentos sin acertar, mostrar que ha perdido y finalizar.
# 10. Opción para poder salir en cualquier momento, y mostrar el número.

print("MUERTOS Y HERIDOS")
import random
import os
lista_resultados = []
# Ciclo para crear numero aleatorio sin repeticion.
numero_pc = ""
bandera_numero_pc = True
while bandera_numero_pc:
    cifra_al_azar = str(random.randint(0,9))
    if cifra_al_azar not in numero_pc:
        numero_pc += cifra_al_azar
    if len(numero_pc) == 4:
        bandera_numero_pc = False
    else:
        bandera_numero_pc = True

# Ciclo principal del juego.
intento = 1
contador = 0
while contador < 15:
    # Ciclo para verificar que el numero del jugador cumpla las condiciones.
    numero_jugador = ""
    bandera_verificacion_numero_jugador = True
    while bandera_verificacion_numero_jugador:
        numero_jugador = str(input("Ingrese su número (no debe repetirse ninguna cifra): "))
        repeticion = -1
        for i in numero_jugador:
            for j in numero_jugador:
                if j == i:
                    repeticion += 1
        if len(numero_jugador) != 4:
            print("Debe ingresar un número de 4 cifras.")
        elif repeticion >= 5:
            print("Las cifras del número no deben repetirse.")
        else:
            bandera_verificacion_numero_jugador = False

    # Conteo de muertos y heridos.
    muertos = 0
    heridos = 0
    for i in range(4):
        if numero_jugador[i] in numero_pc:
            if numero_jugador[i] == numero_pc[i]:
                muertos += 1
            else:
                heridos += 1
    print()
    os.system("cls")
    # Entrega y guardado de resultados:
    resultado = "Intento {}: el número {} tiene {} muerto/s y {} herido/s.".format(intento,numero_jugador,muertos,heridos)
    lista_resultados.append(resultado)
    for i in lista_resultados:
        print(i)
    intento += 1
    contador += 1

    # Ganaste.
    if numero_jugador == numero_pc:
        print("¡GANASTE! El número era {}.".format(numero_pc))
        break

    # Opción para salir.
    salir = True
    # while salir:
    #     salir = str(input('Si quieres salir del programa ingresa "s" y si quieres continuar en el programa ingresa "n": '))
    #     salir = salir.lower()
    #     if salir == "s":
    #         contador = 15
    #         salir = False
    #         print("El número a hallar era {}.".format(numero_pc))
    #     elif salir == "n":
    #         salir = False
    #     else:
    #         print("La opción ingresada no es válida")
    #         salir = True

if contador >= 15:
    print("¡PERDISTE! El número era {}.".format(numero_pc))