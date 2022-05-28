# Programa que pide la edad de un usuario y comprueba que sea menor o mayor de edad. El programa sigue pidiendo la edad hasta que se introduzca un número entero.
bandera = True
while bandera:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad >= 18:
            print("Eres mayor de edad.")
        else:
            print("Eres menor de edad.")
        bandera = False
    except:
        print("No introdujiste un número entero. Vuelve a ingresar tu edad.")

