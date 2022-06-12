# En un examen hay 40 preguntas y cada fallo quita 0.10 puntos. Hacer una funciòn que calcule la nota (en base a 10 puntos) a partir de las preguntas acertadas del examen.
def nota(acertadas):
    return 10 - (40 - acertadas) * 0.10


acertadas = int(input("Ingrese la cantidad de preguntas acertadas: "))

print("Usted obtuvo un {}.".format(nota(acertadas)))