print("========")
print("Conversor")
print("========\n")

print("Menú de opciones:\n")

print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número.\n")

menu = int(input("¿Cuál es tu opción deseada?:"))

if menu == 1:
    print("\n Conversor de número a palabra.")
    numero = int(input("\n ¿Cuál es el número que deseas convertir a palabra?: "))

    if numero ==1:
        print("El número es UNO.")
        print("Fin del programa")
    elif numero == 2:
        print("El número es DOS.")
        print("Fin del programa")
    elif numero == 3:
        print("El número es TRES.")
        print("Fin del programa")
    elif numero == 4:
        print("El número es CUATRO.")
        print("Fin del programa")
    elif numero == 5:
        print("El número es CINCO.")
        print("Fin del programa")
    else:
        print("El número seleccionado no es válido. Intente sólo con números del 1 al 5.")
        print("Fin del programa.")

elif menu == 2:
    print("\n Conversor de palabra a número.")
    numero = input("\n ¿Cuál es la palabra que deseas convertir a número?: ")
    numero = numero.lower()

    if numero == "uno":
        print("El número es 1.")
        print("Fin del programa")
    elif numero == "dos":
        print("El número es 2.")
        print("Fin del programa")
    elif numero == "tres":
        print("El número es 3.")
        print("Fin del programa")
    elif numero == "cuatro":
        print("El número es 4.")
        print("Fin del programa")
    elif numero == "cinco":
        print("El número es 5.")
        print("Fin del programa")
    else:
        print("La opción seleccionada no es válida. Intente sólo con letras minúsculas para escribir un número del uno al cinco.")
        print("Fin del programa.")

else:
    print("La opción ingresada no es válida. Solo debe presionar 1 o 2. Vuelva a a correr el programa.")
