# 1. Muestra todos los elementos de la lista anidada por su índice (mediante bucles for y el tipo range).
# 2. Muestra solo los elementos de las listas con letras.
datos = [
    [1,2,3,4],
    ["a","b","c","d"],
    [5,6,7,8],
    ["e","f","g","h"],
    [9,10,11,12],
    ["i","j","k","l"],
    [13,14,15,16],
    ["m","n","ñ","o"],
]
for i in range(len(datos)):
    for j in range(len(datos[i])):
        print(datos[i][j],end=" ")
    print()

for i in range(len(datos)):
    for j in range(len(datos[i])):
        if isinstance(datos[i][j],str):
            print(datos[i][j],end=" ")
    if isinstance(datos[i][j],str):
        print()