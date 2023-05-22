# Crear una finción llamada removeDuplicates la cual dado un array no ordenado retorna un nuevo array sin elementos duplicados.
# Ejemplo: removeDuplicates ([11,2,5,3,2,3,4,5,1,1,6,6,7])= [1,2,3,4,5,6,7]

# forma inteligencia artificial
def removeDuplicates(arr):
    newArr = []
    for i in range(len(arr)):
        if arr[i] not in newArr:
            newArr.append(arr[i])
    return newArr
print(removeDuplicates([1,1,1,2,3,4,4,4,4,6,6,6]))

# forma Danko:
def removeDuplicates(lista):
    lista_sin_duplicados = []
    for i in lista:
        if i not in lista_sin_duplicados:
            lista_sin_duplicados.append(i)
    return lista_sin_duplicados
print(removeDuplicates([1,1,1,2,2,2,3,3,3,4,4,4,5]))
        