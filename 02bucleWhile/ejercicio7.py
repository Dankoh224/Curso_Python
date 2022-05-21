# Programa que te pide la contraseña y no te deja entrar hasta que la pongas correctamente.
contrasena = "lacholita"
intento = str(input("Ingrese su contraseña: "))
while not contrasena == intento:
    intento = str(input("Las contraseñas no coinciden, vuelva a intentarlo. Ingrese su contraseña: "))
else:
    print("¡Ha ingresado su contraseña con éxito!")