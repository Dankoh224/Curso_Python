#1)  Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
print("\nPrograma 1:")
num = int(input("Ingrese un número entero: "))
suma = 0

while num != 0:
    suma = num + suma
    num = int(input("Ingrese un número entero: "))

print("La suma de todos los valores es " , suma, ". Fin del programa.")

#2)  Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
print("\nPrograma 2:")
num = int(input("Ingrese un número entero: "))
suma = 0

while num != 0:

    if num < 0:
        num = 0
        suma = num + suma
        num = int(input("Ingrese un número entero: "))
        
    else:
        suma = num + suma
        num = int(input("Ingrese un número entero: "))

print("La suma de todos los valores es " , suma, ". Fin del programa.")


#3)  Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
print("\nPrograma 3:")
num = int(input("Ingrese un número entero positivo: "))
x = 0

while num > 0 and num != 0:

    if num > x:
        x = num
        num = int(input("Ingrese otro número entero: "))
        
    else:
        num = int(input("Ingrese un número entero: "))

if num == 0:
    print("El mayor número ingresado es ", x ,". Fin del programa.")

else:
    print("El programa solo funciona para números enteros positivos.")


#4)  Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
print("\nPrograma 4:")
num = int(input("Ingrese un número entero positivo: "))


if num //10 <1:
    print("La suma de las cifras es ",num,".")

elif num //10 >=1 and num //10 <=9:
    cifra1= num // 10
    cifra2 = num % 10
    print("La suma de las cifras es ",cifra1+cifra2,".")
  
elif num//100>=1 and num //100 <=9:
    cifra1= num // 100
    cifra2 = (num % 100)//10
    cifra3= (num % 100)%10
    print("La suma de las cifras es ",cifra1+cifra2+cifra3,".")
else:
    print("El número ingresado es muy grande")

#4b)  Otra forma de hacer el ejercicio anterior.
print("\nPrograma 4b")
suma = 0
n = int(input("Ingrese un número entero positivo: "))

while n > 0:
    x = n%10
    suma = suma + x
    n = n // 10

print("La suma es ", suma,".")
    
