# Encontrar los números repetidos en una lista.
lista = [2,3,5,1,4,3,6,7,9,5,8,3]
lista2 = []
repetidos = []
for i in lista:
    if i not in lista2:
        lista2.append(i)
    else:
        if i not in repetidos:
            repetidos.append(i)
print("Los números repetidos son: {}".format(repetidos))