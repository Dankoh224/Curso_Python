#ejercicio 1
"""contador = 0
for x in range(0,101,3):
    print(x)
    contador = contador + x
print(contador) """

#ejercicio 2
"""factorial = 1
x = int(input("Ingrese un número: "))
for i in range(1,x+1):
    factorial = factorial * i
print("El factorial de ",x," es igual a: ", factorial)"""

#ejercicio 3
"""num1 = 0
num2 = 0
resultado = 0 
for i in range(10):
    if i < 1:
        resultado = num2 + num1
    elif i > 1:
        num1 = num2
        num2 = resultado
        resultado = num2+ num1
    else:
        resultado = resultado + 1
    print(resultado)"""

#ejercicio 4
"""sumapositivos = 0
sumanegativos = 0
n = 0 
for i in range(6):
    x = int(input("Ingrese un número entero: "))
    if x > 0:
        sumapositivos = sumapositivos + x
        n = n + 1
    elif x < 0:
        sumanegativos = sumanegativos + x
    else:
        n = n + 1
    if n == 0:
        n = 1
print("La suma de los negativos es: ",sumanegativos)
print("El promedio de los positivos es: ",sumapositivos/n)"""


