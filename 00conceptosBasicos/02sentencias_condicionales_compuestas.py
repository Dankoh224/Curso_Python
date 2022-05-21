print("Promedieitor: Programa para calcular tu promedio.")

nombre = input("¡Hola! Antes de comenzar, ¿cuál es tu nombre?:  ")

mate = float(input("¿Cómo estas " + nombre + "? Ingresa aquí tu nota de matemática: "))
quimica = float(input("Ahora ingresa tu nota de química: "))
biologia = float(input("Por último, ingresa tu nota de biología: "))

promedio = (mate + quimica + biologia)/3

if promedio >= 4:
    print("Excelente, felicidades " + nombre + ". Aprobaste con un promedio de ", promedio)

    print("Excelente, felicidades " + nombre + ". Aprobaste con un promedio de ", round(promedio,2))
else:
        print("Lo sentimos " + nombre + ". Has reprobado con un promedio de ", promedio)
        print("Lo sentimos " + nombre + ". Has reprobado con un promedio de ", round(promedio,2))

print("Fin.")
