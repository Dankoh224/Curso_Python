# Programa que pide 7 números y comprueba qué número es el mayor.
"""numeroMayor = int(input("Ingresa un número: "))
for i in range(6):
    numero = int(input("Ingresa un número: "))
    if numeroMayor < numero:
        numeroMayor = numero
print(numeroMayor)"""

# Segunda solución:
mayor = None
for i in range(7):
    n = int(input("Ingrese número: "))
    if mayor is None or mayor < n:
        mayor = n
print(mayor)
