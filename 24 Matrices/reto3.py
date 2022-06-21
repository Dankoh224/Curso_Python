# Definir una funcion que dadas dos matrices calcule su suma.
a = [
    [12,53,23,65],
    [43,12,54,65],
    [12,34,43,23]
]

b = [
    [66,45,22,25],
    [56,87,34,64],
    [90,76,76,23]
]

# Función que dadas dos matrices aplica Suma de Matrices.
def sumaMatrices(a,b): 
    matriz = []
    for i in range(len(a)):
        matriz.append([])
        for j in range(len(a[0])):
            suma = a[i][j] + b[i][j]
            matriz[i].append(suma)
    return matriz

for i in a: 
    print("[", end = " ")
    for elemento in i:
        print("{:>4}".format(elemento), end = " ")
    print("]")

print()

for i in b: 
    print("[", end = " ")
    for elemento in i:
        print("{:>4}".format(elemento), end = " ")
    print("]")

print()

c = sumaMatrices(a,b)

for i in c: 
    print("[", end = " ")
    for elemento in i:
        print("{:>4}".format(elemento), end = " ")
    print("]")
