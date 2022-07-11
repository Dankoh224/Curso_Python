# Hacer una agenda telefonica mediante un diccionario
import os
telefonos = {

    "jose": 1234,
    "maria": 2142,
    "andres": 3242,
    "lucia": 3432
}
def menu():
    print()
    print("Mi agenda")
    print("Menu")
    print("1. Consultar.")
    print("2. Ver contactos.")
    print("3. Añadir.")
    print("4. Modificar.")
    print("5. Borrar.")
    print("6. Salir.")
    opcion = str(input("Ingrese opción: "))
    return opcion

def consultar():
    nombre_consulta = str(input("Ingrese nombre para buscar número: "))
    if nombre_consulta in telefonos:
        print("El número de {} es: {}.".format(nombre_consulta,telefonos[nombre_consulta]))
    else:
        print("Ese nombre no está dentro de sus contactos.")

def ver_contactos():
    print("Sus contactos son:")
    contador = 0
    for i in telefonos:
        contador += 1
        print("{}.- {} --> {}.".format(contador,i,telefonos[i]))
    
def anadir():
    nombre_agregado = str(input("Ingrese el nombre del nuevo contacto: "))
    confirmacion_nombre = str(input('¿Está segura/o que desea agregar a {}? Ingrese "s" para continuar o "n" para cancelar: '.format(nombre_agregado)))
    confirmacion_nombre = confirmacion_nombre.lower()

    if confirmacion_nombre == "s" and nombre_agregado not in telefonos:
        numero_agregado = str(input("Ingrese el número de teléfono del nuevo contacto: "))
        confirmacion_numero = str(input('¿Está segura/o de que el número {} es correcto? Ingrese "s" para continuar o "n" para cancelar: '.format(numero_agregado)))
        confirmacion_numero = confirmacion_numero.lower()
        
        if confirmacion_numero == "s":
            telefonos[nombre_agregado] = numero_agregado
        elif confirmacion_numero == "n":
            print("Ok. Vuelva al menu principal y reintente.")
        else:
            print("Error. Solo puede ingresar los caracteres S o N.")

    elif confirmacion_nombre == "n":
        print("Ok. Vuelva al menu principal y reintente.")
    elif nombre_agregado in telefonos:
        print("Ese nombre ya se encuentra entre sus contactos.")
    else:
        print("Error. Solo puede ingresar los caracteres s o n.")

def modificar():
    nombre_modificar = str(input("Ingrese el nombre que desea modificar: "))
    # Ver si el nombre está en el telefono:
    if nombre_modificar in telefonos:
        print("Usted va a modificar la información de {}.".format(nombre_modificar))
        print("Las modificaciones que puede hacer son:")
        print("1. Modificar nombre.")
        print("2. Modificar número.")
        opcion = str(input("Ingrese opción: "))

        # Modificar solo el nombre:
        if opcion == "1":
            nombre_modificado = str(input("Ingrese nuevo nombre para contacto: "))
            confirmacion = str(input('¿Está segura/o de que el nombre {} es correcto? Ingrese "s" para continuar o "n" para cancelar: '.format(nombre_modificado)))
            confirmacion = confirmacion.lower()
            if confirmacion == "s":
                x = telefonos[nombre_modificar]
                del telefonos[nombre_modificar]
                telefonos[nombre_modificado] = x
            elif confirmacion == "n":
                print("Ok. Volverá al menú principal.")
            else:
                print("Error. Solo puede ingresar los caracteres S o N.")
        
        # Modificar el número:
        elif opcion == "2":
            numero_modificado = str(input("Ingrese nuevo número para contacto: "))
            confirmacion = str(input('¿Está segura/o de que el número {} es correcto? Ingrese "s" para continuar o "n" para cancelar: '.format(numero_modificado)))
            confirmacion = confirmacion.lower()
            if confirmacion == "s":
                nombre = nombre_modificar
                del telefonos[nombre_modificar]
                telefonos[nombre] = numero_modificado
            elif confirmacion == "n":
                print("Ok. Volverá al menú principal.")
            else:
                print("Error. Solo puede ingresar los caracteres S o N.")

        # En caso de Error
        else:
            print("Opción incorrecta.")

    else:
        print("Ese nombre no está dentro de sus contactos.")

def borrar():
    nombre_borrar = str(input("Ingrese el nombre que desea borrar: "))
    # Ver si el nombre está en el telefono:
    if nombre_borrar in telefonos:
        print("Usted va a borrar a {} de su celular.".format(nombre_borrar))
        confirmacion = str(input('¿Está seguro que desea borrar la información de este contacto? Ingrese "s" para eliminar el contacto o "n" para cancelar.'))
        if confirmacion == "s":
            del telefonos[nombre_borrar]
        elif confirmacion == "n":
            print("Ok. Volverá al menú principal.")
        else:
            print("Error. Solo puede ingresar los caracteres S o N.")
    else:
        print("Ese nombre no está dentro de sus contactos.")

bandera = True
while bandera:
    opcion = menu()
    if opcion == "1":
        x = consultar()
    elif opcion == "2":
        os.system('cls')
        x = ver_contactos()
    elif opcion == "3":
        x = anadir()
    elif opcion == "4":
        x = modificar()
    elif opcion == "5":
        x = borrar()
    elif opcion == "6":
        print("Ha elegido salir.")
        bandera = False
    else:
        print("Error. Vuelva a intentar")

