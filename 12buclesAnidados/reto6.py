# Cinco amigos van a hacer una carrera: Tomas, Maria, laura, Miguel, Carlos. Muestra todos los posibles resultados que se pueden dar en esta carrera. Es decir, el orden en el que pueden llegar a la meta los cinco amigos. Inlcluye un contador que compruebe cuántas posibilidades se dan.
amigos = ["Tomas", "Maria", "Laura", "Miguel", "Carlos"]
contador = 1
for a in amigos:
    for b in amigos:
        for c in amigos:
            for d in amigos:
                for e in amigos:
                    if a != b and a != c and a != d and a != e:
                        if b != c and b != d and b != e:
                            if c != d and c != e:
                                if d != e:
                                    print(contador,a,b,c,d,e)
                                    contador += 1