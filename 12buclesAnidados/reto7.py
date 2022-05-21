# Para un juego que va a tener 20.000 planetas necesitamos formar nombres para cada uno de ellos. Crea una lista con todos los nombres de tres sílabas que se pueden formar con 10 consonantes y 5 vocales, de tal forma que se intercambien consonante y vocal, y no se repita ninguna letra en cada nombre. Al final muestra la cantidad de nombres de la lista y muestra 10 al azar.
import random
vocales = ["a","e","i","o","u"]
consonantes = ["b","c","d","f","g","h","j","k","l","m"]
contador = 1
nombrePlanetas = []
for a in consonantes:
    for b in vocales:
        for c in consonantes:
            for d in vocales:
                for e in consonantes:
                    for f in vocales:
                        if a != b and a != c and a != d and a != e and a != f:
                            if b != c and b != d and b != e and b != f:
                                if c != d and c != e and c != f:
                                    if d != e and d != f:
                                        if d != f:
                                            x = "{}{}{}{}{}{}".format(a,b,c,d,e,f)
                                            x = x.capitalize()
                                            nombrePlanetas.append(x)
                                            contador += 1
contador2 = 1
listaPlanetas = []
while contador2 <= 10:
    numeroAzar = random.randint(1,43200)
    if nombrePlanetas[numeroAzar] not in listaPlanetas:
        z = "{} --> {}".format(contador2,nombrePlanetas[numeroAzar])
        listaPlanetas.append(z)
        contador2 += 1
print(listaPlanetas)