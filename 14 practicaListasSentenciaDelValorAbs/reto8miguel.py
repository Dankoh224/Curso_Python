# Encuentra el número mayor y el número menor de una lista (la lista puede contener número enteros positivos y números enteros negativos).
# En este caso arreglé el código de Manuel. 
#numeros = [154,22,33,74,54,62,37,28,49]
#numeros = [1,29,-123,-4,5,-6,7,-8,9]
#numeros = [-11,-2,-3,-4,-55,-1,-7,-8,-9]
numeros = []
minimo = 0
maximo = 0
for n in numeros:
    if n > maximo or maximo == 0:
        maximo = n
    if n < minimo or minimo == 0:
        minimo = n
print("El menor es {} y el mayor es {}.".format(minimo,maximo))