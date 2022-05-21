# Crea una lista  nueva que sea el reverso de la lista dada.
numeros = [1,5,8,4,7,2,9]
print(numeros)
lista = list()
for i in range (1,len(numeros)+1):
    lista.append(numeros[len(numeros) - i])
print(lista)

# Tanmbién se puede hacer así:
reverso = list()
for i in numeros:
    reverso = [i] + reverso
print(reverso)

# Y también:
numeros = [1,5,8,4,7,2,9]
print("La lista que veremos ahora es: {}".format(numeros))
reverso = numeros[::-1]
print("Y la lista inversa es: {}".format(reverso))

# O con el método reverse:
numeros = [1,5,8,4,7,2,9]
numeros.reverse()
print(numeros)
