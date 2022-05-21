# PLANTAR UNA BANDERA: es como se le llama a un uso particular de los valores booleanos True y False en un bucle While. Veamos el siguiente ejemplo: realiza un programa que te pida usuario y contraseña y que no te deje entrar hasta que los pongas correctamente.
usuario = "chola"
contrasena = "1234"

entrarSistema = True

while entrarSistema:
    intentoUsuario = str(input("Ingrese usuario: "))
    intentoContrasena = str(input("Ingrese contraseña: "))
    if contrasena == intentoContrasena and usuario == intentoUsuario:
        print("¡MUY BIEN! ¡HAS INGRESADO AL SISTEMA!")
        entrarSistema = False
    else:
        print("Tu usuario o contraseña no son válidos. Vuelve a intentar.")
