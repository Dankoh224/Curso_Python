#Programa que sume los valores pares entre 1 y 20.
n = 2
suma = 0
while 1 < n < 20:
    if n % 2 == 0:
        suma = suma + n
    n = n + 1
print(suma)


