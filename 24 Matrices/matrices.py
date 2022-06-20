# Si queremos hacer una matriz utilizando NUMPY solo debemos importar numpy y usar el numpy.array y darle como argumento una lista:
import numpy
arreglo = numpy.array([1,3,5,7])
print(arreglo)

# También se podría hacer sin numpy y para ello usaríamos bucles for para mostrar los datos que hemos guardado:
consumo = [
    [21,18.75,35,49],
    [19,11,21,144],
    [12,15,1320,30.8]
]
for i in consumo: 
    print("[", end = " ") # Aquí agregamos este corchete y espacio hacia el lado para que se imprima el inicio de nuestra matriz.
    for elemento in i:
        print(elemento, end = " ") # Y acá agregamos la impresión del elemento y de un espacio después de cada elemento, para que quede ordenado.
    print("]") # Finalmente, se agrega el corchete que cerrará cada arreglo.

# También podríamos darle un poco de espacio definido con el método format, en caso de que quisieramos que nos quedara la matriz ordenadita:

for i in consumo: 
    print("[", end = " ")
    for elemento in i:
        print("{:8.2f}".format(elemento), end = " ")
    print("]")

# Por otra parte, una matriz muy particular y utilizada es la matriz cero o nula. Para crear una matriz cero debemos hacer lo siguiente:

matriz_nula = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

for i in matriz_nula: 
    print("[", end = " ")
    for elemento in i:
        print(elemento, end = " ")
    print("]")