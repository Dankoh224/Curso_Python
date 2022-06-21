# Rotar una matriz 90 grados en el sentido contrario al de las manecillas del reloj.
flecha = [
    [0,0,0,0,1,0,0],
    [0,0,0,0,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,0,1,1,0],
    [0,0,0,0,1,0,0],
]

def trasponer(a):
    matriz = []
    for i in range(len(a[0])):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(a[j][len(a[0])-1-i])
    return matriz

c = trasponer(flecha)

for i in c:
    print("[", end = " ")
    for elemento in i:
        print("{:1}".format(elemento), end = " ")
    print("]")

print()

d = trasponer(c)

for i in d:
    print("[", end = " ")
    for elemento in i:
        print("{:1}".format(elemento), end = " ")
    print("]")

print()

e = trasponer(d)

for i in e:
    print("[", end = " ")
    for elemento in i:
        print("{:1}".format(elemento), end = " ")
    print("]")

