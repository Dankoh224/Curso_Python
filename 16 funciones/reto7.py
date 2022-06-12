# Hacer un programa que calcule la nota (en base a 10 puntos) de un examen que puede tener distinta cantidad de preguntas, y por cada fallo se reste una cierta cantidad de puntos.

def nota(cantidad_preguntas,aciertos,fallo):
    nota = (aciertos * 10/cantidad_preguntas) - (cantidad_preguntas - aciertos) * fallo
    return nota

aciertos = 42
cantidad_preguntas = 50
fallos = 0.2
print(nota(cantidad_preguntas,aciertos,fallos))
