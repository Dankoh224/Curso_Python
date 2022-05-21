# Listas Anidadas

nombres = ["susana","ruben","clara","jorge"]
edad = [18,19,20,21]

amigos = [["susana",18],["ruben",19],["clara",20],["jorge",21]]
print(amigos)
print(amigos[0][0]) # Para imprimir se usa la variable y dos corchetes y en su interior, los respectivos índices.

amigos[1][1] = 40
print(amigos)

# Ahora agregaremos un nuevo elemento a la lista amigos.
amigos.append(["sara"])
print(amigos)

# Pero se nos olvidó agregar su edad. Ahora lo haremos:
amigos[4].append(15)
print(amigos)

# Para mostrar la lista mejor organizada:
for i in amigos:
    print("La edad de {} es de {} años".format(i[0],i[1]))