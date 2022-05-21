print("Menú de opciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Módulo o resto")

opcion = int(input("Introduce la opcion deseada: "))

if opcion == 1:
    print("Has elegido sumar.")
    num = int(input("Ingresa el primer valor: "))
    num += int(input("Ingresa el segundo valor: "))
    print("El resultado de tu suma es ",num,".")

elif opcion == 2:
    print("Has elegido restar.")
    num = int(input("Ingresa el primer valor: "))
    num -= int(input("Ingresa el segundo valor: "))
    print("El resultado de tu resta es ",num,".")

elif opcion == 3:
    print("Has elegido multiplicar.")
    num = int(input("Ingresa el primer valor: "))
    num *= int(input("Ingresa el segundo valor: "))
    print("El resultado de tu multiplicación es ",num,".")

elif opcion == 4:
    print("Has elegido dividir.")
    num = int(input("Ingresa el primer valor: "))
    num /= int(input("Ingresa el segundo valor: "))
    print("El resultado de tu división es ",num,".")

elif opcion == 5:
    print("Has elegido dividir de forma entera.")
    num = int(input("Ingresa el primer valor: "))
    num //= int(input("Ingresa el segundo valor: "))
    print("El resultado de tu división entera es ",num,".")

elif opcion == 6:
    print("Has elegido potenciar.")
    num = int(input("Ingresa el primer valor: "))
    num **= int(input("Ingresa el segundo valor: "))
    print("El resultado de tu potencia es ",num,".")

elif opcion == 7:
    print("Has elegido obtener modulo o resto.")
    num = int(input("Ingresa el primer valor: "))
    num %= int(input("Ingresa el segundo valor: "))
    print("El resultado de tu módulo o resto es ",num,".")

else:
    print("La opción ingresada no es válida. Corra nuevamente el programa.")

print("Fin del programa.")
