# Reto rut identificador
rut = str(input("Ingrese su rut sin dígito verificador: "))
dv = str(input("Ingrese el dígito verificador: "))
listaRut = list(rut)
suma = 2*int(listaRut[7])+3*int(listaRut[6])+4*int(listaRut[5])+5*int(listaRut[4])+6*int(listaRut[3])+7*int(listaRut[2])+2*int(listaRut[1])+3*int(listaRut[0])
modulo = suma%11
print(suma)
digitoVerificadorCalculado = 11 - modulo
print(digitoVerificadorCalculado)
if digitoVerificadorCalculado == 11:
    digitoVerificadorCalculado = 0
if digitoVerificadorCalculado == 10:
    digitoVerificadorCalculado = "k"
if str(digitoVerificadorCalculado) == dv: 
    print("Su rut es correcto.")
else:
    print("su rut es incorrecto.")
