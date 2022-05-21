# Hacer un programa en el que haya que elegir una contraseña. La contraseña ha de tener entre 8 y 15 caracteres, una mayuscula y una minuscula, 1 digito y un caracter especial: "·$%$&" Habrá 5 intentos de reestablecer la contraseña, despues de cada intento se indicará la causa si ha sido fallido y al final del quinto intento  se indicará que no ha sido posible establecer la conmtraseña.
caracteres = mayuscula = minuscula = digito = especial = None
contador = 1
while (caracteres == None or mayuscula == None or minuscula == None or digito == None or especial == None) and contador <= 5:
    caracteres = mayuscula = minuscula = digito = especial = None
    print("Intento número {}:".format(contador))
    contrasena = str(input("Ingrese su contraseña: "))
    if 8 <= len(contrasena) <= 15:
        caracteres = True
    if caracteres == None:
        print("No ha alcanzado el largo requerido para la contraseña.")
    for i in contrasena:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mayuscula = True
            break
    if mayuscula == None:
        print("No ha incluido mayúsculas en la contraseña.")
    for i in contrasena:
        if i in "abcdefghijklmnopqrstuvwxyz":
            minuscula = True
            break
    if minuscula == None:
        print("No ha incluido minúsculas en la contraseña.")
    for i in contrasena:
        if i in "0123456789":
            digito = True
            break
    if digito == None:
        print("No ha incluido dígitos en la contraseña.")
    for i in contrasena:
        if i in "$%&@#€Ç€":
            especial = True
            break
    if especial == None:
        print("No ha incluido carácteres especiales en la contraseña.")
    contador += 1
if caracteres == mayuscula == minuscula == digito == especial == True:
    print("La contraseña ha sido reestablecida.")
else:
    print("Ha realizado 5 intentos. No se ha podido reestablecer la contraseña.")
