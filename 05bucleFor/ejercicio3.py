# Programa que comprueba cuántas veces está un número en una lista dada.
lista = [28,36,43,52,61,43,75,84,43,97]
numero = 43
contador = 0
for i in lista:
    if i == numero:
        contador += 1
print("El número {} está {} veces en la lista.".format(numero,contador))