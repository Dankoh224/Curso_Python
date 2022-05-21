# Programa que te pide la contraseña y no te deja entrar hasta que la pongas correctamente.
usuario = "chola"
contrasena = "lacholita"
intentoUsuario = str(input("Ingrese su usuario: "))
intentoContrasena = str(input("Ingrese su contraseña: "))

while (not contrasena == intentoContrasena) or (not usuario == intentoUsuario):
    intentoUsuario = str(input("¡Error! El usuario o la contraseña no coincide, vuelva a intentarlo. Ingrese su usuario: "))
    intentoContrasena = str(input("Ingrese su contraseña: "))
else:
    print("¡Ha ingresado al sistema con éxito!")