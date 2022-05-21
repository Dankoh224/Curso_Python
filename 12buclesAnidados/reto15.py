# Comprobar si la suma de dos números de una lista dan como resultado 10 y mostrar todas las soluciones. No cuenta la suma de un número consigo mismo.
import time
t0 = time.time()
numeros = [2,3,5,8,4,7,6,1]
for i in numeros:
    for j in numeros:
        if i + j == 10 and i != 5:
            print("La suma entre {} y {} da {}.".format(i,j,i+j))
t1 = time.time()
print("El tiempo del programa fue de: {}".format(t1-t0))
print()
t0 = time.time()
for i in numeros:
    if 10 - i in numeros and i != 5:
        print("La suma entre {} y {} da 10.".format(i,10-i))
t0 = time.time()
print("El tiempo del programa fue de: {}".format(t1-t0))
