# Programa que muestra si los números de una lista son positivos o negativos, a excepción del cero que se lo salta.
numeros = [1,4,-3,5,0,7,-2,6]
for i in numeros:
    if i > 0:
        print("El número {} es un número positivo.".format(i))
    elif i < 0:
        print("El número {} es un número negativo.".format(i))
    else:
        continue