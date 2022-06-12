# En el mismo ejercicio anterior, separar en columnas y filas:
figuras = [
    ["cuadrados",6,[3,1]],
    ["círculos",5,[1,2]],
    ["triángulos",4,[2,2]],
    ["rectángulos",3,[4,3]]
]
figuras[0][1] = 5
figuras[0][2] = [1,3]
figuras[3][2][0] = 2
for i in figuras:
    print("{:12} - Cantidad: {:2}  -->  Columna: {}. Fila: {}".format(i[0],i[1],i[2][0],i[2][1]))