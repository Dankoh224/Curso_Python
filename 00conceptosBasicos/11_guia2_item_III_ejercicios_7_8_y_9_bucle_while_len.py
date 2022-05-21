#7)  Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
#Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide,
#indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
#Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
x = 0
frase = str(input("Ingrese una frase: "))
letra = str(input("Ingrese una letra: "))


while x < len(frase):

    if frase[x] == letra:
        print("¡Se encontró una coincidencia! !Está en la posición ",x,"! Veremos si hay otra.")
        x += 1
    else:
        x += 1

print("No hay más coincidencias. Fin del programa.")
    
#8) Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
#(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
#cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto.
#Al finalizar, informar el total a pagar
#Teniendo que cuenta que, si las ventas superan el total de $10000, se le debe aplicar un 10% de descuento.

x = int(input("Ingrese el monto de la compra del cliente: "))
suma = 0

while x == x:    

    if x < 0:
        x = int(input("No se aceptan montos negativos. Ingrese el monto de la compra del cliente: "))
    elif x > 0:
        suma += x
        x = int(input("Ingrese el siguiente monto: "))
    else:
        if suma <= 10000:
            print("Usted a presionado cero. El total a pagar del cliente es de ", suma ," pesos.")
        else:
            print("Usted a presionado cero. El total a pagar del cliente es de ", suma - suma * (10/100) ," pesos.")
        break
        
#9) Crear un programa que solicite el ingreso de números enteros positivos, hasta que
#el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


x = int(input("Ingrese un número entero positivo: "))

while x == x:    

    if x < 0:
        x = int(input("No se aceptan números negativos. Ingrese un número entero positivo: "))

    elif x > 0:
        x = str(x)
        i = 0
        contador = 0
        pares = 0
        impares = 0
        while len(x) > contador:
            if x[i] == "0" or x[i] == "2" or x[i] == "4" or x[i] == "6" or x[i] == "8":
                pares += 1
            if x[i] == "1" or x[i] == "3" or x[i] == "5" or x[i] == "7" or x[i] == "9":
                impares += 1
            contador += 1
            i += 1

        if pares > 1 and impares > 1:
            print("El número ingresado tiene ", pares ," cifras pares y ", impares, " cifras impares.")
        elif pares > 1 and impares == 1:
            print("El número ingresado tiene ", pares ," cifras pares y ", impares, " cifra impar.")
        elif pares == 1 and impares > 1:
            print("El número ingresado tiene ", pares ," cifra par y ", impares, " cifras impares.")
        elif pares == 1 and impares == 1:
            print("El número ingresado tiene ", pares ," cifra par y ", impares, " cifra impar.")
        x = int(input("Ingrese el siguiente número entero positivo: "))

    else:
        print("Usted a presionado cero. Fin del programa")
        break





