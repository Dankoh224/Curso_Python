lista_completa = []
datos_individuales = []
bandera = True
while bandera:
    print("**************************")
    print(" Programa de Verificación ")
    print("           Facial         ")
    print("MENU: ")
    print("1.- para ingresar datos.")
    print("2.- para probar match.")
    print("**************************")
    opcion = input("Ingrese opción del menú: ")

    if opcion == "1":
        try:
            nombre = input("Ingrese su nombre: ")
            d_cejas = float(input("Ingrese la distancia entre sus cejas: "))
            d_lagrimal_ojo = float(input("Ingrese la distancia entre sus lagrimales: "))
            d_comisura_ojo = float(input("Ingrese la distancia entre las comisuras de sus ojos: "))
            d_aletas_nariz = float(input("Ingrese la distancia entre las aletas de su nariz: "))
            d_aleta_nariz_lagrimal_ojo = float(input("Ingrese la distancia entre la aleta de su nariz y el lagrimal de su ojo: "))
            d_centro_nariz_arco_cupido = float(input("Ingrese la distancia entre la punta de su nariz y el arco de cupido: "))
            d_comisuras_labio = float(input("Ingrese la distancia entre las comisuras de sus labios: "))
        
            datos_individuales.append(nombre)
            datos_individuales.append(d_cejas)
            datos_individuales.append(d_lagrimal_ojo)
            datos_individuales.append(d_comisura_ojo)
            datos_individuales.append(d_aletas_nariz)
            datos_individuales.append(d_aleta_nariz_lagrimal_ojo)
            datos_individuales.append(d_centro_nariz_arco_cupido)
            datos_individuales.append(d_comisuras_labio)

            copia_datos_indivisuales = datos_individuales.copy()
            lista_completa.append(copia_datos_indivisuales)
            datos_individuales.clear()
            print(lista_completa)
        except:
            print("No introdujiste un número correcto. Vuelve a intentarlo.")

    elif opcion == "2":
        print(datos_individuales)
        print(lista_completa)
        try:
            nombre = input("Ingrese su nombre: ")
            d_cejas = float(input("Ingrese la distancia entre sus cejas: "))
            d_lagrimal_ojo = float(input("Ingrese la distancia entre sus lagrimales: "))
            d_comisura_ojo = float(input("Ingrese la distancia entre las comisuras de sus ojos: "))
            d_aletas_nariz = float(input("Ingrese la distancia entre las aletas de su nariz: "))
            d_aleta_nariz_lagrimal_ojo = float(input("Ingrese la distancia entre la aleta de su nariz y el lagrimal de su ojo: "))
            d_centro_nariz_arco_cupido = float(input("Ingrese la distancia entre la punta de su nariz y el arco de cupido: "))
            d_comisuras_labio = float(input("Ingrese la distancia entre las comisuras de sus labios: "))
        
            datos_individuales.append(nombre)
            datos_individuales.append(d_cejas)
            datos_individuales.append(d_lagrimal_ojo)
            datos_individuales.append(d_comisura_ojo)
            datos_individuales.append(d_aletas_nariz)
            datos_individuales.append(d_aleta_nariz_lagrimal_ojo)
            datos_individuales.append(d_centro_nariz_arco_cupido)
            datos_individuales.append(d_comisuras_labio)
        except:
            print("No introdujiste un número correcto. Vuelve a intentarlo.")
        
        for i in lista_completa:
            porcentaje_diferencia_cejas = i[1]/d_cejas * 100
            porcentaje_diferencia_lagrimal_ojo = i[2]/d_lagrimal_ojo * 100
            porcentaje_diferencia_comisura_ojo = i[3]/d_comisura_ojo * 100
            porcentaje_diferencia_aletas_nariz = i[4]/d_aletas_nariz * 100
            porcentaje_diferencia_aleta_nariz_lagrimal_ojo = i[5]/d_aleta_nariz_lagrimal_ojo * 100
            porcentaje_diferencia_aleta_centro_nariz_arco_cupido = i[6]/d_centro_nariz_arco_cupido * 100
            porcentaje_diferencia_comisuras_labio = i[7]/d_comisuras_labio * 100
        print(porcentaje_diferencia_cejas)
        print(porcentaje_diferencia_lagrimal_ojo)
        print(porcentaje_diferencia_comisura_ojo)
        print(porcentaje_diferencia_aletas_nariz)
        print(porcentaje_diferencia_aleta_nariz_lagrimal_ojo)
        print(porcentaje_diferencia_aleta_centro_nariz_arco_cupido)
        print(porcentaje_diferencia_comisuras_labio)
    else:
        print("La opción ingresada no es válida.")
    
    bandera = input("¿Desea continuar? Presione S para salir o cualquier tecla para continuar en el programa: ")
    bandera = bandera.lower()
    if bandera == "s":
        bandera = False
    else:
        bandera = True
