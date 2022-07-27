# Hacer una agenda telefonica mediante un diccionario
import os
os.system('cls')

telefonos = {
    "jose": 1234,
    "maria": 2142,
    "andres": 3242,
    "lucia": 3432
}
def menu():
    print()
    print("       Mis Teléfonos")
    print("--------------------------")
    print("1. Consultar por nombre.")
    print("2. Consultar por teléfono.")
    print("3. Listar toda la agenda.")
    print("4. Salir.")
    opcion = str(input("Ingrese opción: "))
    return opcion

def consultar_nombre():
    nombre = str(input("Ingrese el nombre a consultar: "))
    if nombre in telefonos.keys():
        print("El número de {} es {}.".format(nombre,telefonos[nombre]))
    else:
        print("El nombre ingresado no se encuentra dentro de Mis Teléfonos.")
def consultar_telefono():
    try:
        numero = int(input("Ingrese el numero de teléfono a consultar: "))
        contador = 0
        for clave, valor in telefonos.items():
            if numero == valor:
                print("El número {} es de {}.".format(numero,clave))
            else:
                contador += 1
        if contador == len(telefonos.keys()):
            print("El nombre ingresado no se encuentra dentro de Mis Teléfonos.")
    except:
        print("No se acepta el ingreso de caracteres que no sean numéricos")
def listar_agenda():
    numero = 0
    print()
    print("      Mi Lista")
    print("--------------------")
    for clave, valor in telefonos.items():
        numero += 1
        print("{}. {}: {}.".format(numero,clave,valor))

bandera = True
while bandera:
    opcion = menu()
    if opcion == "1":
        x = consultar_nombre()
    elif opcion == "2":
        x = consultar_telefono()
    elif opcion == "3":
        x = listar_agenda()
    elif opcion == "4":
        print("Ha elegido salir.")
        bandera = False
    else:
        print("Error. Vuelva a intentar")