#5) Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen.
#La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
print("\nPrograma 5")
suma = 0
n = 0
z = 0

while n != -1:

    n = int(input("Ingrese un número entero positivo: "))
    suma = 0

    if n%2 == 0:
        z += 1
       
    if n != -1:
        while n > 0:
            x = n%10
            suma = suma + x
            n = n // 10
        print("La suma de las cifras del número es ", suma,".")

print("El número -1 finaliza el programa. La cantidad de números pares ingresados son ", z ,". Fin del programa.")

#6) Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa.
#A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error.
#El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto.
#Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

print("Menú de opciones:\n1) Comenzar programa. \n2) Imprimir listado. \n3) Finalizar programa.")
opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion != 3:

    while opcion !=3:
        if opcion == 1:
            print('La opción elegida fue "comenzar programa", por lo tanto iniciaremos el programa. \nComenzando programa...\nCargando...')
        elif opcion == 2:
            print('La opción elegida fue "imprimir listado":\nImprimiendo listado...\nMarcos\nManuel\nXimena\nRicardo\nDanko\nFin del listado.')
        else:
            print("La opción elegida no es válida. Ingrese una opción válida.")

        opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion ==3:
    print("Fin del programa.")


        
 
