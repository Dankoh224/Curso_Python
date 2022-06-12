# Aplanar lista

lista = [[1,2,3],[4,5,6],[8]]
listaPlana = []
for i in lista:
    for elemento in i:
        listaPlana.append(elemento)
print(listaPlana)

# ¿Cómo hacerlo si la lista tiene un objeto no iterable (int)?

lista = [[1,2,3],4,[5,6],8]
listaPlana = []
for i in lista:
    if type(i) == int:
        listaPlana.append(i)
    else:
        for elemento in i:
            listaPlana.append(elemento)
print(listaPlana)

lista = [[1,2,3],4,[5,6],8]
listaPlana = []
for i in lista:
    if isinstance(i,int):
        listaPlana.append(i)
    else:
        for elemento in i:
            listaPlana.append(elemento)
print(listaPlana)