# Programa una función que convierta segundos a horas, minutos. Que pida segundos 
# y muestre el resultado.

def segundos (seg):
    return seg//3600, seg%3600//60, (seg%3600)%60
a,b,c = segundos(int(input("Ingrese la cantidad de segundos a convertir: ")))
print("Los segundos ingresados equivalen a {}:{}:{}.".format(a,b,c))

