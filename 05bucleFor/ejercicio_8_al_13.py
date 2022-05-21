#ejercicio 8: calcular la suma de todos los n números enteros ingresados, la suma de los pares y la suma de los impares.
"""sumapares = 0
sumaimpares = 0
suman = 0
n = int(input("Ingrese cantidad números: "))
for i in range (1,n+1):
    x = int(input("Ingrese número: "))
    suman = suman + x
    if x%2==0:
        #es par
        sumapares=sumapares+x
    else:
        sumaimpares=sumaimpares+x
print("Suma n ingresados: ",suman)
print("Suma pares: ",sumapares)
print("Suma impares: ",sumaimpares)"""

#ejercicio9: contar los divisores de un número y mostrarlos en pantalla.
"""x = int(input("Ingrese número: "))
contador = 0
for i in range (1,x+1):
    if x%i==0:
        print(i)
        contador = contador + 1
print("Hay", contador, "divisores.")"""

#ejercicio 10: contar los votos de n personas y determinar el ganador de 2 equipos de futbol (peru vs argentina).
"""n = int(input("Cantidad de personas que votan: "))
print("Para votar por Perú presione 1.")
print("Para votar por Argentina presione 2.")
argentina = 0
peru = 0

for i in range(1,n+1):
    x = int(input(f"Ingrese el voto de la persona {i}: ))
    while x != 1 and x != 2:
        x = int(input("La opción ingresada no es válida. Intente de nuevo: "))
    if x == 1:
        peru = peru + 1
    else:
        argentina = argentina + 1
print("Los votos para Perú son ",peru,"y para argentina son ",argentina,".")
if argentina > peru:
    print("El ganador es Argentina.")
elif argentina < peru:
    print("El ganador es Perú.")
else:
    print("Argentina y Perú han empatado.")"""

#ejercicio 11: Ingresar 4 notas, mostrarlos en una lista y calcular el promedio.
"""suma_notas = 0
L = []
for i in range(4):
    nota = float(input("Ingrese nota: "))
    L.append(nota)
    suma_notas = suma_notas + nota
print(L)
promedio = suma_notas/4
print("Promedio = ",promedio)"""

#ejercicio 12: Ingresar N notas, mostrarlos en una lista y calcular el producto de todos sus valores.
"""n = int(input("ingrese la cantidad de notas: "))
L = []
for i in range(1,n+1):
    num = float(input("Ingrese número: "))
    L.append(num)
print(L)
producto = 1
for i in L:
    producto = producto * i
print("Producto: ",producto)
L.insert(2,354)
print(L)"""

#ejercicio 13: Ingresar N notas, mostrar en listas los números pares de forma ascendente y de forma descendente los
#números impares.
"""n = int(input("Cantidad de notas: "))
L = []
M = []
for i in range(n):
    num = float(input("Ingrese nota: "))
    if num % 2 == 0:
        L.append(num)
    else:
        M.append(num)
L.sort()
M.sort()
M.reverse()

print(L)
print(M)"""
