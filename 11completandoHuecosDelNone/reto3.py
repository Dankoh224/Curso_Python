# Ingresar 7 numeros e identificar cual de ellos es el mayor.
mayor = None
for i in range(1,8):
    numero = int(input("Ingresa el nº {}: ".format(i)))
    if mayor is None or mayor < numero:
        mayor = numero
print("El número mayor es {}.".format(mayor))