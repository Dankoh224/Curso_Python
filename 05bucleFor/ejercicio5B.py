# Haz un programa que compruebe si un elemento esta en una lista y nos diga en qué posición (índice) se encuentra.
lista = [2,5,90,23,45,87,54,11,38]
elemento = 90
for i in range(len(lista)):
    if lista[i] == elemento:
        print("El elemento {} está en la posición {}.".format(elemento,i))