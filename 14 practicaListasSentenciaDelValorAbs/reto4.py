# Programa que informa del número de datos que se han recogido. Pide el número de datos que se mantienen y deja esos datos empezando por los primeros, y borra el resto (utilizar la sentencia del).
datos = [1.12,2.18,1.45,2.21,3.07,2.32,3.41,1.39]
print("La cantidad de datos que se han recogido son {}.".format(len(datos)))
cantidadDeDatosQueSeMantienen = int(input("¿Cuántos datos desea mantener?: "))
del datos[cantidadDeDatosQueSeMantienen:]
print(datos)