# METODOS: 
# print(dir(dict))


d = {"animal": "perro","color":"blanco","edad":4}


# Metodo GET: se usa para no tener que hacer un if & else para corregir el error de que no se encuentre la clave. Primer argumento indica la clave, segundo argumento entrega un mensaje de error.
# print(d.get("animal","Esta clave no existe."))

# Este método puede servir por ejemplo para hallar las unidades de ciertos articulos de un inventario:
inventario = {
    "tornillos": 100,
    "tuercas": 12,
    "arandelas": 323,
}

articulo = str(input("Ingrese nombre articulo: "))
cantidad = inventario.get(articulo,0)
print("{}: {}".format(articulo,cantidad))

# MÉTODO ZIP: Si quisieramos convertir dos listas en un diccionario, solo usaremos el método zip. 
letras = ["A","B","C","D","E"]
numeros = [1, 2, 3, 4, 5]
diccionario = dict(zip(letras,numeros))
print(diccionario)


