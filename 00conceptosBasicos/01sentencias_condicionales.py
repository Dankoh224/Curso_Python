print("Sistemas para calcular el promedio de un alumno.")

nombre = input("Hola, cuál es tu nombre?: ")

mate = int(input(nombre + ", ingresa tu promedio de matemática: "))
quimica = int(input(nombre + ", ahora ingresa tu promedio de química: "))
biologia = int(input(nombre + ", finalmente ingresa tu promedio de biología: "))

promedio = (mate + biologia + quimica)/3
promedio = int(promedio)

if promedio >= 4:
    print(nombre + ", felicidades, aprobaste tu año escolar con un ", promedio, ".", promedio)

print("Fin del programa...")
