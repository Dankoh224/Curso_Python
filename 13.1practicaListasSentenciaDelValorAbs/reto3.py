# Progama que borra los elementos repetidos de una lista y solo quedan los elementos unicos, ninguno repetido.
numeros = [1,2,3,4,5,3,4,6,5,7,8,1,2,3,4,4,4,0]
for i in numeros:
    for j in range(len(numeros)-1,numeros.index(i),-1):
        if i == numeros[j]:
            numeros.remove(numeros[j])
print(numeros)