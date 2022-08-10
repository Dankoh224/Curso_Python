import numpy as np
# La siguiente función me entrega un número aleatorio entre 0 y 1 excluyendo al 1. Sin embargo, si al argumento le entrego un valor entero (solo puede ser entero), se genera un arreglo con esa cantidad de números aleatorios:
aleatorio = np.random.random(1)
print(aleatorio)

# Para generar números aleatorios siguiendo una distribución normal estándar:
aleatorio = np.random.normal(0,1,10)
print(aleatorio)

# Para generar numeros aleatorios enteros hacemos lo siguiente:
arreglo = np.random.randint(1,11,10)
print(arreglo)