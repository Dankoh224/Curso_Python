# MÉTODO SETDEFAULT: Cuando usamos el método get, si queremos imprimir por pantalla un articulo que no está dentro del diccionario, no arrojará ningun error, ejemplo:
inventario = {
    "tornillos": 100,
    "tuercas": 12,
    "arandelas": 323,
}
articulo = input("Ingrese el articulo: ")
unidades = inventario.get(articulo,0)
print("{}: {}".format(articulo,unidades))
#Sin embargo, existe un método que permite guardar de forma automática el valor que NO está dentro del diccionario, junto con un valor por defecto. Esto se hace con el método "setdefault".
articulo = input("Ingrese el articulo: ")
unidades = inventario.setdefault(articulo,0)
print("{}: {}".format(articulo,unidades))
print("        Inventario")
for clave, valor in inventario.items():
    print("{}: {}".format(clave, valor))
# Si se observa bien, el primer artículo no queda grabado dentro del diccionario, no así al usar el método setdefault.
