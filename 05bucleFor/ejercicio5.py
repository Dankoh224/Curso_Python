# Haz un programa que compruebe si un elemento esta en una lista y nos diga en qué posición (índice) se encuentra.
lista = [2,5,90,23,45,87,54,11,38]
elemento = 7
contador = 0
for i in lista:
    if elemento == i:
        print("El elemento {} está en la posición {}.".format(elemento,contador))
    contador += 1    
if elemento not in lista:
    print("El elemento no está en la lista.")