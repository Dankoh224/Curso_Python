# En un exámen hay 40 preguntas y cada fallo quita 0.1 puntos.
# hacer una función que calcule la nota (en base a 10 puntos) a 
# partir de las preguntas acertadas al exámen.
def nota (acertadas):
    return 0.25 * acertadas - 0.1 * (40 - acertadas)
print(nota(int(input("Ingrese cantidad de aciertos: "))))