# Crea una baraja con bucles añadiendo las cartas a una lista mediante bucles for.
numero = ["As","2","3","4","5","6","7","8","9","10","jota","quena","kaiser"]
pinta = [" de corazón"," de diamante"," de pica"," de trébol"]
baraja = []
for i in numero:
    for j in pinta:
        carta = i + j
        print(carta)
        baraja.append(carta)
for i in range(0,52,4):
    print("{:10}  {:10}  {:10}  {:10}".format(baraja[i],baraja[i+1],baraja[i+2],baraja[i+3]))