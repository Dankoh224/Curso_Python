#1) Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
print("\nPrograma 1:")
contrasena1 = str(input("Ingrese su contraseña: "))
contrasena2= str(input("Vuelva a ingresar su contraseña para confirmar que es correcta: "))

while contrasena1 != contrasena2:
    contrasena1 = str(input("Error. Las contraseñas no coinciden. Ingrese su contraseña nuevamente:"))
    contrasena2= str(input("Vuelva a ingresar su contraseña: "))

print("Muy bien, puedes acceder al sitio. Fin del programa.")


#2) Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar.
#A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
#El programa no comprobará que las cantidades sean positivas.

print("\nPrograma 2:")
ahorro_total = int(input("Ingrese la cantidad total de dinero que quiere obtener: "))
ahorro_parcial = 0

while ahorro_parcial < ahorro_total:
    ahorro_parcial = ahorro_parcial + int(input("Ingrese la cantidad de dinero que ahorrará para llegar a la meta: "))
    meta = ahorro_total - ahorro_parcial
    print("Ahora le faltan ", meta," pesos para llegar a la meta de ", ahorro_total, " pesos. ")

print("Felicidades, ha llegado a la meta de ahorro. Ha ahorrado ", ahorro_total, " pesos.")

#3) Escriba un programa que mejore la simulación de la hucha del ejercicio anterior, no permitiendo que se escriban cantidades negativas.

print("\nPrograma 3:")
ahorro_total = int(input("Ingrese la cantidad total de dinero que quiere obtener: "))
ahorro_parcial = 0

while ahorro_parcial < ahorro_total:
    ingreso = int(input("Ingrese la cantidad de dinero que ahorrará para llegar a la meta: "))

    if ingreso < 0:
        print("No se pueden ingresar cantidades negativas.")
    else:
        ahorro_parcial = ahorro_parcial + ingreso
        meta = ahorro_total - ahorro_parcial
        print("Ahora le faltan ", meta," pesos para llegar a la meta de ", ahorro_total, " pesos. ")

print("Felicidades, ha llegado a la meta de ahorro. Ha ahorrado ", ahorro_total, " pesos.")

#4) Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos
#contraseñas coincidan, con un límite de tres peticiones.

print("\nPrograma 4:")
print("Cuidado, solo tiene 3 intentos para ingresar.")
contrasena1 = (input("Ingrese su contraseña: "))
contrasena2= (input("Vuelva a ingresar su contraseña para confirmar que es correcta: "))
x = 1
y = 2

while contrasena1 != contrasena2 and x < 3 :
    if y == 1:
        y = str(y)
        contrasena1 = str(input("Error. Las contraseñas no coinciden. Le queda " + y + " intento. Ingrese su contraseña nuevamente:"))
        contrasena2= str(input("Vuelva a ingresar su contraseña: "))
        x +=1
        y = 1
    else:
        y = str(y)
        contrasena1 = str(input("Error. Las contraseñas no coinciden. Le quedan " + y + " intentos. Ingrese su contraseña nuevamente:"))
        contrasena2= str(input("Vuelva a ingresar su contraseña: "))
        x +=1
        y = 1
if contrasena1 != contrasena2:
    print("Lo sentimos, no puedes acceder al sitio. Fallaste los 3 intentos. Fin del programa.")
else:
    print("Muy bien, puedes acceder al sitio. Fin del programa.")


