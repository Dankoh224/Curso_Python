# Hacer un programa en el que haya que elegir una contraseña. La contraseña ha de tener entre 8 y 15 carácteres, 1 mayúscula, una minúscula, 1 dígito y un carácter especial: "&$%". Habrá 5 intentos de establecer la contraseña y después de cada intento se indicará la causa si ha sido un intento fallido. Al final del 5to intento se indicará que no ha sido posible establecer la contraseña.
contador = 5
mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minuscula = "abcdefghijklmnñopqrstuvwxyz"
digito = "0123456789"
caracter = "$%&"
checkLargo = False
checkMayuscula = False
checkMinuscula = False
checkDigito = False
checkCaracter = False
cantidadMayuscula = 0
cantidadMinuscula = 0
cantidadDigito = 0
cantidadCaracter = 0
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
            cantidadMayuscula += 1
    if cantidadMayuscula > 0:
        checkMayuscula = True    
    else:
        print("¡ERROR! La contraseña debe tener al menos una letra Mayúscula. Te quedan {} intentos.".format(contador))
        continue
    for i in contrasena:
        if i in minuscula:
            cantidadMinuscula += 1
    if cantidadMinuscula > 0:
        checkMinuscula = True    
    else:
        print("¡ERROR! La contraseña debe tener al menos una letra Minúscula. Te quedan {} intentos.".format(contador))
        continue
    for i in contrasena:
        if i in digito:
            cantidadDigito += 1
    if cantidadDigito > 0:
        checkDigito = True    
    else:
        print("¡ERROR! La contraseña debe tener al menos un Número. Te quedan {} intentos.".format(contador))
        continue
    for i in contrasena:
        if i in caracter:
            cantidadCaracter += 1
    if cantidadCaracter > 0:
        checkCaracter = True    
    else:
        print("¡ERROR! La contraseña debe tener al menos un Dígito Especial. Te quedan {} intentos.".format(contador))
        continue
    if checkLargo and checkMayuscula and checkMinuscula and checkDigito and checkCaracter:
        break
if contador == 0:
    print("No ha sido posible reestablecer la contraseña. Fin del programa.")
else:
    print("Se ha reestablecido la contraseña.")