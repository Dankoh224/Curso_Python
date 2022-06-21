# Programa que crea una matriz con los datos que introduces: Filas, columnas y valores para cada elemento.
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valores = str(input("Ingrese un valor para la fila {}, columna {}: ".format(i+1,j+1)))
        if valores in "1234567890":
            valores = int(valores)
        matriz[i].append(valores)

for i in matriz: 
    print("[", end = " ")
    for elemento in i:
        print("{:>8}".format(elemento), end = " ")
    print("]")