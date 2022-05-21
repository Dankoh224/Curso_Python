# Programa tablas de multiplicar del 2 a 7
factor1 = ["2","3","4","5","6","7"]
factor2 = ["1","2","3","4","5","6","7","8","9","10"]
for i in factor2:
    for j in factor1:
        resultado = int(i) * int(j)
        print("{:2}* {:2} = {:2} ; ".format(i,j,resultado), end="")
    print()