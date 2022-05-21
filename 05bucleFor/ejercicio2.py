# Programa que pida un número al usuario. Si ese número más algún número de la lista dada es igual a  100, el programa dice que el número cumple la condición.
lista = [28,36,43,52,61,75,84,97]
num = int(input("Ingrese número: "))
continuar = False
for i in lista:
    if i + num == 100:
        continuar = True
if continuar:
    print("El número cumple con la condición.")
else:
    print("El número NO cumple con la condición.")