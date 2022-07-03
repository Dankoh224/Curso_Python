# programa que simula una calculadora utilizando funciones que tenga las opciones sumar restar multiplicar y dividir:
from unittest import result


def menu():
    print("*****************")
    print("   Calculadora   ")
    print("                 ")
    print(" 1. Sumar        ")
    print(" 2. Restar       ")
    print(" 3. Multiplicar  ")
    print(" 4. Dividir      ")
    print(" 5. Salir        ")
    print("                 ")
    opcion = (input("Ingrese la opción: "))
    return opcion

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b


x = 0
bandera = True
while bandera:
    print("Nueva operación:")
    print()
    x = menu()
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    if x == "1":
        resultado = sumar(a,b)
    elif x == "2":
        resultado = restar(a,b)
    elif x == "3":
        resultado = multiplicar(a,b)
    elif x == "4":
        resultado = dividir(a,b)
    elif x == "5":
        print("Gracias por usar el programa.")
        break
    else:
        print("Opción incorrecta. Vuelve a intentar.")


    while x == "1" or x == "2" or x == "3" or x == "4": 
        print()
        print("Resultado:",resultado)
        print()
        seguir = str(input("¿Quiere continuar operando con el resultado? S/N: "))
        print()
        if seguir.lower() == "n":
            break
        else:
            x = menu()
            a = resultado
            b = int(input("Ingrese el siguiente número: "))
            if x == "1":
                resultado = sumar(a,b)
            elif x == "2":
                resultado = restar(a,b)
            elif x == "3":
                resultado = multiplicar(a,b)
            elif x == "4":
                resultado = dividir(a,b)
            elif x == "5":
                print("Gracias por usar el programa.")
                bandera = False
                break
            else:
                print("Opción incorrecta. Vuelve a intentar.")