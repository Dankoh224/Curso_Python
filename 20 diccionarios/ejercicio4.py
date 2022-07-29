# Contador de letras: programa que cuenta la cantidad de cada una de las letras que aparecen en una frase.
frase = "Hoy ha salido el sol y hace una mañana estupenda"
diccionario = {}
for i in frase.lower():
    contador = 0
    if i == " ":
        continue
    elif i not in diccionario:
        diccionario[i] = 1
    else:
        diccionario[i] += 1
for clave, valor in diccionario.items():
    print("{}: {}.".format(clave, valor))