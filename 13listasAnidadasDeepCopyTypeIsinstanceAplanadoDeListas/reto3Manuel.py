# Crear listas anidadas mediante el esquema de la cajonera del dibujo del reto 3.
cajonera = [
    [
        [["A",5],["B",0],["C",7],["D",2],["E",9]],
        [["F",5],["G",5],["H",4],["I",5],["J",4]],
        [["K",1],["L",8],["M",1],["N",8],["Ñ",5]],
    ],
    [
        [["O",3],["P",0],["Q",6],["R",3],["S",2]],
        [["T",3],["U",2],["V",6],["W",5],["X",1]],
        [["Y",7],["Z",3],[" ",0],[" ",0],[" ",0]]
    ]
] #Aqui Manuel crea una lista con dos listas: Cajonera1 y Cajonera2. Dentro de cada una crea 3 listas más (las filas) y en cada una se encuentran 5 listas (las columnas). Dentro de estás se encuentra el elemento letra y el elemento cantidad. 

for cajon in cajonera:
    for fila in cajon:
        for columna in fila:
            print("{}:{} ".format(columna[0],columna[1]), end="")
        print()
    print()
