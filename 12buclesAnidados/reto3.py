# Crea una baraja con bucles añadiendo las cartas a una lista mediante bucles for.
numero = ["As","2","3","4","5","6","7","8","9","10","jota","quena","kaiser"]
pinta = [" de corazón"," de diamante"," de pica"," de trébol"]
baraja = []
for i in numero:
    for j in pinta:
        carta = i + j
        baraja.append(carta)
for i in range(0,52,4):
    for j in range(4):
        print(" {:20} ".format(baraja[i+j]), end="")
    print()