# Crear una lista con 10000 números al azar y encontrar los números repetidos.
import random
import time
t0 = time.time()
contador = 1
lista = []
while contador <= 10000:
    x = random.randint(1,10000)
    lista.append(x)
    contador += 1
print("La cantidad de números de la lista es: {}".format(len(lista)))
repetidos = []
listaNueva = []
for i in lista:
    if i not in listaNueva:
        listaNueva.append(i)
    else:
        if i not in repetidos:
            repetidos.append(i)
print("Los números repetidos son: {}".format(repetidos))
print("La cantidad de números que se repiten son: {}".format(len(repetidos)))
t1 = time.time()
print("La cantidad empleada para correr el programa es de:",t1-t0)