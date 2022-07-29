# Contador de letras: programa que cuenta la cantidad de cada una de las letras que aparecen en una frase.
frase = "Hoy ha salido el sol y hace una mañana estupenda"
diccionario = {}
for letra in frase.lower():
    if letra == " ":
        continue
    diccionario.setdefault(letra,0)
    diccionario[letra] += 1
for letra, cantidad in diccionario.items():
    print("{}: {}.".format(letra, cantidad))