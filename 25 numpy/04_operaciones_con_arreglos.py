# Suma, resta, multiplicación y todo de arreglos
import numpy as np

a = np.arange(1,11)
print(a)
print(a**3) # Aquí ya puedo hacerle practicamente lo que quiera al arreglo completo.

# Crear arreglos con el mismo número:
b = np.ones(10)
print(b)
print(b**2)

# Sumar arreglos entre arreglos (solo si tienen la misma cantidad de elementos)
print(a*2 + b)

# Comparar arreglos
print(a == b)
print(a > b)

# Sumar todos los elementos del arreglo:
print(a.sum())

# Promediar todos los elementos de un arreglo:
print(a.mean())

# Hallar el mínimo y máximo de un arreglo:
print(a.min())
print(a.max())