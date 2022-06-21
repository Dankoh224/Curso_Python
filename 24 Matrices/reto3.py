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
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        matriz = []
        for i in range(len(a)):
            matriz.append([])
            for j in range(len(a[0])):
                suma = a[i][j] + b[i][j]
                matriz[i].append(suma)
        return matriz
    else:
        return None

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

if c == None:
    print("No se pueden sumar las matrices. No son de igual orden.")
else:   
    for i in c: 
        print("[", end = " ")
        for elemento in i:
            print("{:>4}".format(elemento), end = " ")
        print("]")
