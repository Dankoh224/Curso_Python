# Crea una matriz cero de orden 10 * 15 de forma automática
for i in range(15):
    print("[",end=" ")
    for j in range(10):
        print("0",end=" ")
    print("]")

# Otra forma de hacer una matriz de 10 * 15, es como lo hizo el profe Manuel:
matrizCero = [[0] * 15] * 10
matrizCero[0][0] = 12
for i in matrizCero:
    print(i)
# Sin embargo este método nos entrega la misma lista repetida una y otra vez, por lo que si quisieramos cambiar un elemento de la lista, se cambiaría el elemento de esa posición en todas las filas. Así que si el primer elemento de la primera fila lo cambiamos por 12, todos los primeros elementos de las filas se transformarían en 12.

# Entonces, para que la lista no se repita, y podamos agregar un elemento en cualquier posición de la lista, haremos lo siguiente:
matrizCero = []
for i in range(10):
    matrizCero.append([0]*15)
matrizCero[0][0] = 12
matrizCero[9][14] = 12
for i in matrizCero:
    print(i)