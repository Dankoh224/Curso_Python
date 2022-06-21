# Crear una copia del arreglo del reto 1 y muestre:
# Elemento mayor
# Elemento menor
# Suma de los elementos
# Promedio de los elementos
# Mostrar todos los elementos
import numpy as np
a = np.random.randint(0,101 ,10)
print(a)

b = a[:].copy()
print(b)
print(b.max())
print(b.min())
print(b.sum())
print(b.mean())
for i in b:
    print(i)






