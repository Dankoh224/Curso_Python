'''#4)  Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco).
#Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea.
#Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea).
#Finalmente, informar cuántas líneas completas se ingresaron.

linea = ""
contador = 0
libro = str(input('Ingrese el nombre del libro. Digite "/ " si desea dar por completada una linea. Digite "*" si desea finalizar el programa.'))

while contador == contador:
    if libro != "/" and libro != "*":
        linea += libro
        print(linea)
        libro = str(input('Ingrese el nombre de otro libro. Digite "/ " si desea dar por completada una linea. Digite "*" si desea finalizar el programa.'))  
        
    elif libro == "/":
        i = 0
        num = 0
        cifras = 0
        while num < 10:
            num = str(num)
            if linea[i] == num:
                cifras += 1
                num = 0
                i += 1
            if linea[i] != num:
                num = int(num)
                num += 1
            
        print('Usted ingresó el símbolo "/". Se ha completado una línea. Existen ',cifras,' cifras númericas en los títulos de los textos de esta línea.')
        libro = str(input('Ingrese el nombre de otro libro. Digite "*" si desea finalizar el programa.'))

    elif libro == "*":
        print('Ha ingresado el símbolo "*". Ha finalizado el programa.')

    else:
        print("La opción ingresada no es válida.")
        break'''
            
#5)  Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
#Imprimir la cantidad de números primos ingresados.

#6) Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera)
#y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

linea = ""
contador = 0
libro = str(input('Ingrese el nombre del libro. Digite "/ " si desea dar por completada una linea. Digite "*" si desea finalizar el programa.'))

i = 0
print(libro[i])
num = 0
cifras = 0
while num < 10:
    num = str(num)
    if libro[i] == num:
        cifras += 1
        num = 0
        i += 1
    else:
        num = int(num)
        num += 1
    print('Usted ingresó el símbolo "/". Se ha completado una línea. Existen ',cifras,' cifras númericas en los títulos de los textos de esta línea.')


    libro = str(input('Ingrese el nombre de otro libro. Digite "*" si desea finalizar el programa.'))

# Git Push probar