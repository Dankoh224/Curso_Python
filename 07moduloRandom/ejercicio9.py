# Calcula la suma de los números del 1 al millón: Hazlo con while y con for y mide el tiempo de ejecución.
import time
inicio = time.time()
contador = 0
suma = 0
while contador <= 1000000:
    suma += contador
    contador += 1
print(suma)
final = time.time()
print("El tiempo transcurrido es de {} segundos.".format(final-inicio))

inicio = time.time()
suma = 0
for i in range(1000001):
    suma += i
print(suma)
final = time.time()
print("El tiempo transcurrido es de {} segundos.".format(final-inicio))
