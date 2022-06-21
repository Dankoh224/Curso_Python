# Definir una función que dadas dos matrices calcule su multiplicación.
a = [
    [1,2],
    [3,4],
    [5,6]
]

b = [
    [1,2,3],
    [4,5,6]
]

# Esta multiplicación es de 2x3 y 3x2 Por lo tanto se obtiene una tabla de 2x2.

def multiMatrices(a,b):
    if len(a[0]) == len(b):
        matriz = []
        for i in range(len(a)): # 0x0,0x1,1x0,1x1
            matriz.append([])
            for j in range(len(b[0])):
                elemento = 0
                for k in range(len(a[0])):
                    multi = a[i][k] * b[k][j]
                    elemento = elemento +  multi
                matriz[i].append(elemento)
        return matriz
    else:
        return None

c = multiMatrices(a,b)

for i in c:
    print("[", end = " ")
    for elemento in i:
        print("{:3}".format(elemento), end = " ")
    print("]")