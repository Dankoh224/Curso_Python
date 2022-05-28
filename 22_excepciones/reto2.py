# Programa que lleva a cabo una división.
while True:
    try:
        dividendo = float(input("Ingresa el primer número de la división: "))
        divisor = float(input("Ingresa el segundo número de la división:"))
        division = dividendo / divisor

    except ValueError:
        print("Valor ingresado incorrecto. Debes ingresar un valor numérico.")
    except ZeroDivisionError:
        print("No puedes dividir por cero")
    else:
        print(division)
        print("Fin del programa.")
        break
