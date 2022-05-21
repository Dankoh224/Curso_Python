#Haz un programa con una función que muestre un saludo, dando la bienvenida al
#usuario, utilizando su nombre, el cual se ha pedido antes de llamar la función.
#La función no devuelve nada (es decir, devuelve None). Definir la función con
#un parámetro (el nombre del usuario).

def saludo (nombre):
    print("Hola {}, bienvenido al programa.".format(nombre) )
    return None
nombreDelUsuario = input("Introduzca su nombre: ")
saludo(nombreDelUsuario) 