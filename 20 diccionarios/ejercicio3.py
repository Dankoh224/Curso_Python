# Convertir un diccionario en dos listas.
pares = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
lista_letras = []
lista_numeros = []
for clave, valor in pares.items():
    lista_letras.append(clave)
    lista_numeros.append(valor)
print(lista_letras)
print(lista_numeros)


# Convertir dos listas en un diccionario. 
letras = ["A","B","C","D","E"]
numeros = [1, 2, 3, 4, 5]
diccionario = {}
for i in range(len(letras)):
    diccionario[letras[i]] = numeros[i]
print(diccionario)