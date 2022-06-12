# Programa que comprueba si una cadena de caracteres es un palindromo.
cadena = "alla va mi m av allá"
cadena = cadena.lower()
cadena = cadena.replace(",","").replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

reverso = cadena[::-1]

print(cadena)
print()
print(reverso)
print()
if cadena == reverso:
    print("El texto ES un palíndromo")
else:
    print("El texto NO es un palíndromo")

