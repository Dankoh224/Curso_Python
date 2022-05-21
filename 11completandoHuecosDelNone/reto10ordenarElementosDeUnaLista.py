# Para ordenar una lista se puede hacer de las siguientes fomrmas:

lista = [2,1,3]
listaOrdenada = list(lista)
listaOrdenada.sort()
print(listaOrdenada)
print(lista)
print(id(lista))
print(id(listaOrdenada))


lista = [2,1,3]
listaOrdenada = sorted(lista)
print(listaOrdenada)
print(lista)
print(id(lista))
print(id(listaOrdenada))