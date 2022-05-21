#Programa que te pide que introduzcas un número que esté entre el 10 y el 20. Si es correcto, debe decir "estás en el rango" y te pida otro. Hasta que le des un número que esté fuera del rango y se acabe el programa.
x = int(input("Introduce un número entre 10 y 20: "))
while 10 < x < 20:
    print("¡Estás en el rango!")
    x = int(input("Introduce otro número entre 10 y 20: "))
print("Fin del programa.")

