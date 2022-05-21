# En una loteria hay un bombo que tiene 10 bolas con los numeros del 1 al 10. En un sorteo se sacan 5 bolas, sin que se introduzcan las bolas que se han sacado previamente. Haz un programa que muestre todas las apuestas posibles, es decir, todas las combinaciones posibles que se pueden dar en esa lotería. Incluye un contador para comprobar el número de combinaciones que se dan.
bolas = [1,2,3,4,5,6,7,8,9,10]
contador = 0
lista = []
for a in bolas:
    for b in bolas:
        for c in bolas:
            for d in bolas:
                for e in bolas:
                    if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
                        x = [a,b,c,d,e]
                        x.sort()
                        if x not in lista:
                            lista.append(x)
                            contador += 1
print(lista)
print(contador)