# Crear filas anidadas mediante el esquema de la cajonera del dibujo del reto 3.
cajonera = [
    [
    [["A",5],["B",0],["C",7],["D",2],["E",9]],
    [["F",5],["G",5],["H",4],["I",5],["J",4]],
    [["K",1],["L",8],["M",1],["N",8],["Ñ",5]]
    ],
    [
    [["O",3],["P",0],["Q",6],["R",3],["S",2]],
    [["T",3],["U",2],["V",6],["W",5],["X",1]],
    [["Y",7],["Z",3],[" ",0],[" ",0],[" ",0]]
    ]
]
print()
print("===========================================================================================================")
print("                                                 INVENTARIO                                                ")
print("===========================================================================================================")

for cajon in cajonera:
    for fila in cajon:
        for elemento in fila:
            print("Letra {}: {:3} unidades   ".format(elemento[0],elemento[1]), end="")
        print()
    print()
opcion = None
letra = ""
cantidad = 0
while opcion == None:
    print("====================================================")
    print("MENU:")
    print("Ingresa 1 si deseas sacar una letra del inventario.")
    print("Ingresa 2 si deseas agregar una letra al inventario.")
    print("Ingresa 3 si deseas salir del menu.")
    print("====================================================")
    print()
    opcion = int(input("Ingresa el número de la opción de tu preferencia: "))
    if opcion == 1 or opcion == 2:
        if opcion == 1:
            opcionLetra = str(input("¿Qué letra vas a sacar?: "))
            cantidad = int(input("¿Cuántas letras vas a sacar?: "))
            for cajon in cajonera:
                for fila in cajon:
                    for grupo in fila:
                        if grupo[0] == opcionLetra:
                            grupo[1] -= cantidad
                            opcion = None
                            break  
        if opcion == 2:
            opcionLetra = str(input("¿Qué letra vas a agregar?: "))
            cantidad = int(input("¿Cuántas letras vas a agregar?: "))
            for cajon in cajonera:
                for fila in cajon:
                    for grupo in fila:
                        if grupo[0] == opcionLetra:
                            grupo[1] += cantidad
                            opcion = None
                            break               
    elif opcion == 3:
        print("Programa finalizado. La nueva fila de inventario se imprimirá a continuación:")
        print("Gracias por usar InventariEitor")
    else:
        print("OPCIÓN INVÁLIDA. VUELVE A INTENTARLO.")
        opcion = None
print("===========================================================================================================")
print("                                          INVENTARIO ACTUALIZADO                                           ")
print("===========================================================================================================")

for cajon in cajonera:
    for fila in cajon:
        for elemento in fila:
            print("Letra {}: {:3} unidades   ".format(elemento[0],elemento[1]), end="")
        print()
    print()