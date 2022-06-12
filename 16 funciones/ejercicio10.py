# Haz un programa que simule calculadora utilizando funciones (multiplicar, dividir,
# sumar, restar).

encendido = int(input(('Para encender la calculardora, presiona "1"...')))
if encendido == 1:
    print("####################################")
    print("##    BIENVENIDO A CALCULADORA    ##")
    print("####################################")
    print("¿Qué deseas hacer?")
def sumar (a,b):
    return a + b
def restar (a,b):
    return a - b
def multiplicar (a,b):
    return a * b
def dividir (a,b):
    return a / b

def menu ():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = int(input("Ingrese opción: "))
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    if opcion == 1:
        resultado = sumar(n1,n2)
    elif opcion == 2:
        resultado = restar(n1,n2)
    elif opcion == 3:
        resultado = multiplicar(n1,n2)
    elif opcion == 4:
        resultado = dividir(n1,n2)
    return resultado

print(menu())