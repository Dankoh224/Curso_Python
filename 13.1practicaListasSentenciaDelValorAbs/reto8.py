# Encuentra el número mayor y el número menor de una lista (la lista puede contener número enteros positivos y números enteros negativos).
#numeros = [154,22,33,74,54,62,37,28,49]
#numeros = [1,29,-123,-4,5,-6,7,-8,9]
#numeros = [-11,-2,-3,-4,-55,-1,-7,-8,-9]
distancia = 0
minimo = 0
maximo = 0
numeros = []
for i in numeros:
    for j in numeros:
        if abs(i-j) > distancia:
            minimo = i
            maximo = j
            distancia = abs(i-j) 
if minimo > maximo:
    menor = maximo
    mayor = minimo
    print("El número mínimo es {} y el máximo es {}.".format(menor,mayor))
else:
    print("El número mínimo es {} y el máximo es {}.".format(minimo,maximo))