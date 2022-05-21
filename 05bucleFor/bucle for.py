"""suma = 0
for i in range (101):
    suma = i + suma

print(suma)"""

frase = input("Ingrese una frase")
contador = 0
for x in frase:
    if x in "aeiou":
        contador = contador + 1
print("La cantidad de vocales es: ", contador)
    
