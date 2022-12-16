# dado un conjunto de numeros y un valor objetivp, debes devolver el indice de los dos números que suman el objetivo. Solo usa un bucle.
d = [2,4,3,6,12,23]
o = 16
for i in d:
    if (o - i) in d:
        print(d.index(i),d.index(o-i))
        break