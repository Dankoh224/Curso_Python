# Programa que pide datos (tratamiento, nombre y apellido) de las personas que han sido invitadas a una fiesta, para enviarles una carta de invitación. Luego se muestra en pantalla la carta con los datos que se piden y se pregunta si se quiere introducir nuevos datos de otra persona.
continuar = True
while continuar:
    tratamiento = str(input("Ingrese cuál es su trato con el organizador de la fiesta: "))
    nombre = str(input("Ingrese su nombre: "))
    apellido = str(input("Ingrese su apellido: "))
    print("*************************************************")
    print("*************************************************")
    print("* De: Cami y Danko                              *")
    print("* Para: {} {}.                                  *".format(nombre,apellido))
    print("*                                               *")
    print("*             TARJETITA DE INVITACIÓN           *")
    print("*                                               *")
    print("* Hola {} ¿como estás? Deseamos que te encuen-  *".format(tratamiento))
    print("* tres súper. Te escribimos para invitarte con  *")
    print("* mucho cariño a nuestra fiesta. Ojalá asistas. *")
    print("*                                               *")
    print("*                 ¡Nos vemos!                   *")
    print("*                                               *")
    print("*************************************************")
    print("*************************************************")
    continuar = str(input("¿Desea continuar igresando invitados? S/N: "))
    continuar = continuar.lower()
    if continuar == "n":
        continuar = False