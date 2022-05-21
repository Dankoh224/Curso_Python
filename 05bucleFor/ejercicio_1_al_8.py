#ejercicio1: Pedir 10 números, sumarlos y mostrar el resultado.
"""total = 0
for i in range(10):
    x = int(input("Ingresa un número: "))
    total = total + x
print(total)"""

#ejercicio2: Pedir números hasta que salga uno negativo. Mostrar que cantidad de números ingresaron.
"""total = 0
x = float(input("Ingresa un número positivo, si ingresas un número negativo se detendrá el programa: "))
while x >= 0:
    total = total + 1
    x = float(input("Ingresa el siguiente valor: "))
print("Ingresaste", total, "valores.")"""

#ejercicio3: Pedir un número y mostrar su tabla hasta el diez.
"""x = int(input("Ingresa un número: "))
for i in range(1,11):
    print(i*x)"""

#ejercicio4: Pedir dos números y  mostrar  todos los números impares comprendidos entre ellos.
"""num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
while num1 == num2:
    print("No existe ningún valor entre estos dos números. Ingrese valores distintos")
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))
if num1%2 == 0:
    #num1 es un número par
    if num2 % 2 == 0:
        #num1 y num2 son pares, entonces:
        while num1 < (num2 - 2):
            num1 = num1 + 2
            print(num1)
    else:
        #num1 es par y num2 impar, por lo tanto:
        while num1 < (num2 - 2):
            num1 = num1 + 2
            print(num1) 
else:
    #num1 es un número impar
    if num2 % 2 == 0:
        #num1 es impar y num2 es par, entonces:
        num1 = num1 + 1
        print(num1)
        while num1 < (num2 - 2):
            num1 = num1 + 2
            print(num1)
    else:
        #num1 y num2 son impar, por lo tanto:
        num1 = num1 + 1
        print(num1)
        while num1 < (num2 - 2):
            num1 = num1 + 2
            print(num1)     
print("Fin del programa.")"""

#ejercicio4: Pedir dos números y  mostrar  todos los números impares comprendidos entre ellos (FOR IN).
"""num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
while num1 >= num2:
    print("El primer valor debe ser menor que el segundo valor.")
    num1 = int(input("Ingrese primer valor: "))
    num2 = int(input("Ingrese segundo valor: "))
for i in range (num1 + 1,num2):
    if i % 2 == 0:
        print(i)
    else:
        x = 0
print("Fin del programa.")"""

#ejercicio5: Hallar la suma de los cuadrados de los primeros n números naturales.
"""n = int(input("Ingrese el número n: "))
total = 0
while n <= 0:
    n = int(input("El número n debe ser positivo. Ingrese nuevamente el valor n:"))
for i in range (n+1):
    total = total + i**2
print("La suma de los cuadrados de los primeros n números es: ", total)"""

#ejercicio6: Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
#finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""compuesto = 0
cantidad_primos = 0
x = int(input("Ingrese un número mayor que 1: "))
while x !=0:
    if x > 1:
        for i in range (2,x):
            if x % i == 0:
                #x es un número compuesto
                compuesto = compuesto + 1
            else:
                n = 0
        if compuesto != 0:
            print("El número",x,"es un número compuesto.")
        else:
            cantidad_primos = cantidad_primos + 1
            print("El número",x,"es un número primo.")
        compuesto = 0
    else:
        print("El número debe ser mayor que 1.")
    
    x = int(input("Ingrese el siguiente valor: "))

if x == 0:
    print("Fin del programa. La cantidad total es de", cantidad_primos, "números primos.")"""

#ejercicio6: Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
#finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados (variables booleanas).

"""n = int(input("Número: "))
cantidad = 0
while n != 0:
    primo = True
    for i in range (2,n):
        if n % i == 0:
            primo = False
            break
    if primo == True:
        cantidad = cantidad + 1
    n = int(input("Número: ")) 
print("Primos: ", cantidad)"""

#ejercicio 7: Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese
#rango, que sean bisiestos y multiplos de 10. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser
#divisible por 100, excepto que sea divisible por 400.
"""año1 = int(input("Ingrese primer año: "))
año2 = int(input("Ingrese segundo año: "))
for i in range (año1 + 1, año2):
    if (i % 4 == 0 and i % 100 != 0 and i % 10 == 0) or i % 400 == 0:
        print(i)"""

#ejercicio 7: Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese
#rango, que sean bisiestos y multiplos de 10. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser
#divisible por 100, excepto que sea divisible por 400.
"""año1 = int(input("Ingrese primer año: "))
año2 = int(input("Ingrese segundo año: "))

for i in range (año1 + 1, año2):
    if not i % 10 == 0:
        continue
    if not i % 4 == 0:
        continue
    if i % 100 == 0:
        continue
    print(i)""""

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
        sumapares=sumapares+1
    else:
        sumaimpares=sumaimpares+1
print("Suma n ingresados: ",suman)
print("Suma pares: ",sumapares)
print("Suma impares: ",sumaimpares)""":
    



    
