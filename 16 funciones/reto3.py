# Define una función que concatene dos cadenas de carácteres, las veces que le indiquemos. Hacer un programa que pida dos cadenas y las veces que han de repetirse, y mostrar el resultado en pantalla.
def concatenar (cadena1,cadena2,veces):
    return (cadena1 + cadena2) * veces

# Programa:
cadena1 = str(input("Ingrese la primera cadena de carácteres: "))
cadena2 = str(input("Ingrese la segunda cadena de carácteres: "))
veces = int(input("¿Cuántas veces se deben repetir: "))
print(concatenar(cadena1,cadena2,veces))