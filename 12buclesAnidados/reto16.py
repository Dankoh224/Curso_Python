# Comprobar si la suma de dos números de una lista de 100.000 de números al azar, dan como resultado 10 y mostrar todas las soluciones. No cuenta la suma de un número consigo mismo.
import random
import time
numeros =[]
for i in range(100000):
    n = random.randint(1,100000000)
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        numeros.append(n)
t0 = time.time()
for i in numeros:
    for j in numeros:
        if i + j == 100000000 and i != j:
            print("La suma entre {} y {} da {}.".format(i,j,i+j))
t1 = time.time()
print("El tiempo del programa fue de: {}".format(t1-t0))

print()
t0 = time.time()
for i in numeros:
    if 100000000 - i in numeros and 100000000 / 2 != i:
        print("La suma entre {} y {} da 100000000.".format(i,100000000-i))
t1 = time.time()
print("El tiempo del programa fue de: {}".format(t1-t0))