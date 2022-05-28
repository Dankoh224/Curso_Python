# Realizar programa que administra una lista de compra.
listaDeCompras = []

menu = True
while menu:
    print("Menu:")
    print("1) Ver lista.")
    print("2) Ingresar producto.")
    print("3) Eliminar producto.")
    print("4) Salir del programa.")
    print("Ingrese el número de la opción que desea:")

    menu = int(input())
    if menu == 1:
        print("La lista de compras en este momento es:")
        print(listaDeCompras)
    elif menu == 2:
        producto = str(input("Ingrese el nombre del producto que agregará a la lista: "))
        listaDeCompras.append(producto)
    elif menu == 3:
        producto = str(input("Ingrese el nombre del producto que quitará de la lista: "))
        if producto in listaDeCompras:
            listaDeCompras.remove(producto)
        else:
            print("El producto que usted quiere remover no se encuentra en la lista de compras. Vuelva a intentar.")
    elif menu == 4:
        print("Gracias por usar ListeilorDeCompreteitor")
        break
    elif type(menu) == str:
        print("Opción inválida.")
    else:
        print("Opción inválida.")
        