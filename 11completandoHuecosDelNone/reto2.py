# Ingresar 7 numeros e identificar cual de ellos es el mayor.
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))
n4 = int(input("Ingresa el cuarto número: "))
n5 = int(input("Ingresa el quinto número: "))
n6 = int(input("Ingresa el sexto número: "))
n7 = int(input("Ingresa el séptimo número: "))
mayor = None
if mayor is None:
    mayor = n1
if mayor < n2:
    mayor = n2
if mayor < n3:
    mayor = n3
if mayor < n4:
    mayor = n4
if mayor < n5:
    mayor = n5
if mayor < n6:
    mayor = n6
if mayor < n7:
    mayor = n7
print("El número mayor es {}.".format(mayor))