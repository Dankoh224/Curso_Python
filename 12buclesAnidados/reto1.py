# Crea una baraja con bucles añadiendo las cartas a una lista mediante bucles for.
numero = ["As","2","3","4","5","6","7","8","9","10","jota","quena","kaiser"]
pinta = ["de corazón","de diamante","de pica","de trébol"]
baraja = []
for i in range(len(numero)):
    for j in range (len(pinta)):
        baraja.append("{} {}".format(numero[i],pinta[j]))
print(baraja)

for i in numero:
    for j in pinta:
        print("{} {}.".format(i,j))