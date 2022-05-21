#ejercicio 14: ingresar N números, determinar los números primos.
"""n = int(input("Ingrese la cantidad de números: "))
for i in range(n):
    num = int(input("Ingrese número: "))
    contador = 0
    for x in range(1,num+1):
        if num % x == 0:
            contador = contador + 1
    if contador > 2:
        print("El número ",num," es un número compuesto.")
    else:
        print("El número ",num," es un número primo.") """

#ejercicio 15: Determinar el mayor número de N valores ingresados.
"""n = int(input("Ingrese cantidad de números: "))
L = []
for i in range(n):
    num = int(input("Ingrese número: "))
    L.append(num)
L.sort()
print(L[n-1])"""

#ejercicio 16: Determinar el menor número de N valores ingresados.
"""n = int(input("Ingrese cantidad de números: "))
L = []
for i in range(n):
    num = int(input("Ingrese número: "))
    L.append(num)
L.sort()
print(L[0])"""

#ejercicio 17: Calcular el factorial de un número.
"""n = int(input("Ingrese número: "))
resultado = 1
for i in range(1,n+1):
    resultado = resultado*i
print(resultado)"""

#ejercicio 18: Escribir una frase y contar  la cantidad de vocales que aparece en dicha frase.
"""frase = str(input("Ingrese frase: "))
cantidad = 0
for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cantidad = cantidad + 1
print("Hay ",cantidad,"vocales.")"""

#ejercicio 19: Mostrar los años bisiestos encontrados en un intervalo de años.
"""a = int(input("Ingrese límite inferior: "))
b = int(input("Ingrese límite superior: "))

for i in range(a,b+1):
    if i % 4 == 0 and i % 100 != 0:
        print(i)
    elif i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
        print(i)
    else:
        x = 0"""

#ejercicio 20: mostrar en pantalla los números de fibonacci según sus N términos.
"""n = int(input("Ingrese cuántos números desea imprimir de la secuencia: "))
num1 = 0
num2 = 1
sig = 0
print(num1)
print(num2)

for i in range(n-2):
    sig = num1 + num2
    print(sig)
    num1 = num2
    num2 = sig"""

#ejercicio 21: Escribir una oración y mostrar en pantalla las vocales que aparecen (sin repetir las vocales).
oracion = str(input("Ingrese la oración: "))
oración = list(oracion)
for i in oracion: 
        if oracion.count(i) >= 2:
            del oracion[0]
        else:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                print(i)

