# Instrucciones: Desarrolle los enunciados, aplicando los contenidos vistos en la clase.
# Ejercicio 1:
# Crear un arreglo unidimensional con nombre arregloA y de tamaño 100, con elementos aleatorios de números enteros del 0 al 500, luego:
# Mostrar por pantalla sólo los valores que se encuentren en los índices pares del arreglo.
# Mostrar el elemento mayor del arreglo.
# Mostrar el índice (posición) del elemento mayor.
# Mostrar el elemento menor del arreglo.
# Generar la copia de arreglo A y multiplicar por 3 cada elemento. Mostrar resultado.
# Mostrar la suma de los elementos del segundo arreglo.
# Calcular el promedio de los elementos del segundo arreglo.
from turtle import pos
import numpy as np
arregloA = np.random.randint(1,501,100)
print(arregloA)
print()
for i in range(len(arregloA)):
    if i % 2 == 0:
        print(arregloA[i], end = " ")
print()
print()
mayor = arregloA.max()
posicionMayor = np.where(arregloA == mayor)
for i in posicionMayor:
    posicionMayor = i[0]

print("El número mayor del arreglo es {} y su posición es {}.".format(arregloA.max(),posicionMayor))
print("El elemento menor del arreglo es {}.".format(arregloA.min()))

arregloB = arregloA[:].copy()
print(arregloB * 3)
print("La suma del arreglo B es {}.".format(arregloB.sum()))
print("El promedio del arreglo B es {}.".format(arregloB.mean()))