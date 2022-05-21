# Programa que pide un número de inicio y otro final al usuario y que suma todos los números múltiplos de 3 que hay entre ellos.
x = int(input("Ingrese un número para el límite inferior: "))
y = int(input("Ingrese un número como límite superior: "))
suma = 0
while x <= y:
    if x % 3 == 0:
        suma = suma + x
    x = x + 1
print(suma)



