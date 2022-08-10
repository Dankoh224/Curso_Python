import numpy as np
# ¿Cómo hallar todos los indices de un array?
array = np.array([12,22,15,4,5,6])
print(np.where(array == 1)) # No se encuentra
print(np.where(array > 5)) # Solo mayores a 5
print(np.where(array == array.min() )) #Solo el mayor
