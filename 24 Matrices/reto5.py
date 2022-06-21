# Trasponer los elementos de las filas a las columnas y viceversa.

a = [
    [1,2],
    [3,4],
    [5,6]
]

b = [
    [1,2,3],
    [4,5,6]
]

def trasponer(a):
    matriz = []
    for i in range(len(a[0])):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(a[j][i])
    return matriz

c = trasponer(b)

for i in c:
    print("[", end = " ")
    for elemento in i:
        print("{:1}".format(elemento), end = " ")
    print("]")


