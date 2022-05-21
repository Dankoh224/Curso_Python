#Realizar un algoritmo que permita al usuario ingresar N números enteros, los cuales pueden ser 
#positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el producto
#de los positivos.
n = int(input("Ingrese el número N: "))
sumaPositivos = 0
productoNegativos = 1
for i in range(n):
    num = int(input("Número: "))
    if num > 0:
        sumaPositivos = sumaPositivos + num
    elif num < 0:
        productoNegativos = productoNegativos * num
    else:
        print("Este número no es válido.")
print("La suma de los positivos es ",sumaPositivos, "y el producto de los negativos es ",productoNegativos,".")