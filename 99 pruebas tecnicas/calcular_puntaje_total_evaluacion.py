# Una empresa que realiza pruebas de selección de personal, necesita conocer el puntaje total obtenido por los candidatos que presenten las pruebas técnicas a un determinado empleo. El puntaje total se calcula restando del puntaje obtenido por respuestas correctas, el obtenido por respuestas incorrectas y en blanco. Por cada respuesta correcta se obtienen 5 puntos, respuesta incorrecta -2 puntos y respuesta en blanco -1 punto. La cantidad total de preguntas que tiene la evaluación son de 20.
respuestas_correctas = int(input('Ingrese respuestas correctas: '))
respuestas_incorrectas = int(input('Ingrese respuestas incorrectas: '))
respuestas_en_blanco = int(input('Ingrese respuestas en blanco: '))

puntaje_total = respuestas_correctas * 5 - respuestas_incorrectas * 2 -respuestas_en_blanco * 1

print('El puntaje obtenido por el estudiante es ',puntaje_total)
