# Hacer un programa en el que haya que elegir una contraseña. La contraseña ha de tener entre 8 y 15 carácteres, 1 mayúscula, una minúscula, 1 dígito y un carácter especial: "&$%". Habrá 5 intentos de establecer la contraseña y después de cada intento se indicará la causa si ha sido un intento fallido. Al final del 5to intento se indicará que no ha sido posible establecer la contraseña.
contador = 5
mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minuscula = "abcdefghijklmnñopqrstuvwxyz"
digito = "0123456789"
caracter = "$%&"
checkLargo = checkMayuscula = checkMinuscula = checkDigito = checkCaracter = False
while contador > 0:
    contador -= 1
    contrasena = str(input("Ingrese contraseña: "))
    if 8 <= len(contrasena) <= 15:
        checkLargo = True
    else:
        print("¡ERROR! La contraseña debe tener un largo de 8 a 15 carácteres. Te quedan {} intentos.".format(contador))
        continue
    for i in contrasena:
        if i in mayuscula:
            checkMayuscula = True 
        if i in minuscula:
            checkMinuscula = True 
        if i in digito:
            checkDigito = True
        if i in caracter:
            checkCaracter = True   
    if checkLargo and checkMayuscula and checkMinuscula and checkDigito and checkCaracter:
        break
    else:
        if not checkMayuscula:
            print("¡ERROR! La contraseña debe tener al menos una letra Mayúscula. Te quedan {} intentos.".format(contador))
        elif not checkMinuscula:
            print("¡ERROR! La contraseña debe tener al menos una letra Minúscula. Te quedan {} intentos.".format(contador))
        elif not checkDigito:
            print("¡ERROR! La contraseña debe tener al menos un Número. Te quedan {} intentos.".format(contador))
        elif not checkCaracter:
            print("¡ERROR! La contraseña debe tener al menos un Dígito Especial. Te quedan {} intentos.".format(contador))
        continue
if contador == 0:
    print("No ha sido posible reestablecer la contraseña. Fin del programa.")
else:
    print("Se ha reestablecido la contraseña.")