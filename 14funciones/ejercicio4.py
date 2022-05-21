#Define una función que concatene dos cadenas de carácteres, las veces que indiquemos.
#Hacer un programa que pida dos cadenas y las veces que han de repetirse y mostrar el resultado 
#en pantalla.
def concatenar (cadena1, cadena2, veces):
    return (cadena1 + cadena2)*veces
print(concatenar(str(input("Ingrese la primera cadena: ")),str(input("Ingrese segunda cadena: ")), int(input("Ingrese cantidad de veces a repetir concatenación: "))))