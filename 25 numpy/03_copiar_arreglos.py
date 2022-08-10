import numpy as np

# Para copiar un arreglo:

a = np.random.randint(0,101 ,10)
print(a)
b = a[:] # Con esto copiamos lo que queramos.
print(b)

print(id(a)) # Aquí se puede ver que tienen distintos ID (no son los mismos objetos).
print(id(b))

# Sin embargo, si hago un cambio al arreglo original o a la copia, se realiza automáticamente el cambio en ambos arreglos:

b[0]=12
print(a)
print(b)

# Si necesito que sean arreglos completamente independientes, usaremos la función .copy(). De esta forma no se nos cambiarán ambos arreglos:

c = a[:].copy()
print(id(a))
print(id(c))

c[2] = -14
print(a)
print(c)
