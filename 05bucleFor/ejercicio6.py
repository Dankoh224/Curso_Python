# Programa que muestra la tabla de multiplicar de un número que le demos.
num = int(input("Ingrese un número: "))
for i in range (1,11):
    total = num * i
    print("{} x {} = {}".format(num,i,total))