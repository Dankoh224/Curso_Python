# Hacer un programa que calcule  la nota (en base a 10 puntos) de 
# un exámen que puede tener distinta cantidad de preguntas. Por
# cada fallo se resta una cierta cantidad de puntos.
def nota (cantidadPreguntas,aciertos,puntajeEnContra):
    return (10/cantidadPreguntas)*aciertos - (cantidadPreguntas-aciertos)*puntajeEnContra

cantidadDePreguntas = int(input("Ingrese la cantidad de preguntas de la prueba: "))
aciertos = int(input("ingrese la cantidad de aciertos de su prueba: "))
puntajeEnContra= float(input("Ingrese la cantidad en contra por cada pregunta: "))
print(nota(cantidadDePreguntas,aciertos,puntajeEnContra))