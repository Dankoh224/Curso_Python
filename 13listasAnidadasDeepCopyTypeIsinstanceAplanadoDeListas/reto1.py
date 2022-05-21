# En una tienda quieren hacer un inventario de las figuras que tienen y el número de unidades de cada una. Crea una lista que contenga los datos del inventario: 6 cuadrados, 5 círculos, 4 triángulos y 3 rectángulos.
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
    print("{:12}: {:2} unidades. Cesta: {}".format(i[0],i[1],i[2]))