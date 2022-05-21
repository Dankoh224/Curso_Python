# Programa un juego que permita hacer todas las operaciones que se pueda entre dos valores al azar en 10 segundos.
import time
import random
reInicio = "si"
puntajeMaximo = 0
nombre = "Vacío"
while reInicio == "si":
    print("********************************************")
    print("* Bienvenidos al Juego de Velocidad Mental *")
    print("*               de Danko                   *")
    print("********************************************")
    print("Puntaje Máximo: {}. Jugador: {}.".format(puntajeMaximo,nombre))
    print("El juego es muy simple hijo, solo responde las operaciones lo más rápido que puedas. Intenta no quedar en un puesto demasiado mediocre maldición.")
    nombre = str(input("Ingresa tu Alias (si sabes escribir): "))
    comenzar = str(input('Para comenzar tu pobre intento, presiona "Enter": '))
    correctas = 0
    if comenzar == "":
        jugar = True
    else:
        jugar = False
    while jugar:
        inicio = time.time()
        while jugar:
            final = time.time()
            if final - inicio >= 60:
                jugar = False
                break
            else:
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
                operacion = random.choice(["+","-","x",":"])
                print(num1,operacion,num2,"=")
                intento = int(input(""))

                final = time.time()
                if final - inicio >= 60:
                    print("Has tardado demasiado en responder la última operación po penquita.")
                    jugar = False
                    break

                if operacion == "+":
                    resultado = num1 + num2
                    if intento == resultado:
                        print("¡Correcto!")
                        correctas += 1
                    else:
                        print("¡Incorrecta!")
                elif operacion == "-":
                    resultado = num1 - num2
                    if intento == resultado:
                        print("¡Correcto!")
                        correctas += 1
                    else:
                        print("¡Incorrecta!")
                elif operacion == "x":
                    resultado = num1 * num2
                    if intento == resultado:
                        print("¡Correcto!")
                        correctas += 1
                    else:
                        print("¡Incorrecta!")
                elif operacion == ":":
                    resultado = num1 // num2
                    if intento == resultado:
                        print("¡Correcto!")
                        correctas += 1
                    else:
                        print("¡Incorrecta!")
    if correctas == 0:
        print("Tiempo Utilizado: 0")
        print("Respuestas correctas: 0")
        print("Fin del Juego")

    else:
        print("Tiempo Utilizado:",round(final - inicio,2))
        print("Respuestas correctas:",correctas)
    
    if correctas > puntajeMaximo:
        puntajeMaximo = correctas
        print("Pfff... Aunque solo era operatoria básica, has obtenido el puntaje más alto de la competencia ¡Felicidades!")
    
    reIngreso = True
    reInicio = str(input('Escribe "SI" si quieres volver a jugar o "NO" si no quieres volver a jugar: '))
    reInicio = reInicio.lower()
    while reIngreso:
        if reInicio != "no" and reInicio != "si":
            reInicio = str(input('No seas idiota, escribe claramente  "SI" o "NO" maldito.. ¡Diantres!'))
            reInicio = reInicio.lower()
        else:
            reIngreso = False

else:
    print("¡¡¡CHAO PENQUITAS!!!")