# Crea una lista "cuenta adelante" que contenga los elementos de la lista "cuenta atras" pero en orden inverso. Utiliza el método reverse.
cuentaAtras = [10,9,8,7,6,5,4,3,2,1,0]
print("Cuenta atrás es: {}".format(cuentaAtras))
cuentaAdelante = list(cuentaAtras)
cuentaAdelante.reverse()
print("Cuenta adelante es: {}".format(cuentaAdelante))
