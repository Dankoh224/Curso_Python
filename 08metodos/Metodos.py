# Métodos vs funciones
# ¿Cuál es la diferencia entre métodos y funciones?. La principal diferencia es que un método es parte de una clase, es decir, es parte de la funcionalidad que le damos a un objeto. Por tanto, siempre va a estar asociado a un objeto. Sin embargo, las funciones en Python, están definidas por si mismas y no pertenecen a ninguna clase.
# Al ser intrínsecos al objeto en sí, cada objeto tiene sus propios métodos. Incluso aunque se llamen igual, pueden tener un significado distinto. Por ejemplo, el método index está disponible para los objetos string y list. Sobre una cadena de caracteres, da el índice de la letra en esa palabra, sobre una lista, da la posición de un elemento en una lista.

# Clase STR.
# Método STRIP: elimina espacios u otros carácteres SI Y SOLO SI estos se encuentran a los lados del string. Ejemplo:
respuesta = " s  "
respuesta = respuesta.strip()
print(respuesta)

saludo = "Hola,"
saludo = saludo.strip(",")
print(saludo)

nombre = ".Manuel..."
nombre = nombre.strip(".")
print(nombre)

# Método SPLIT: separa una cadena de caracteres, según el argumento que le demos, convirtiendo la cadena en una lista y los carácteres en elementos de una lista. Ejemplo:
tiempo = "Hace un hermoso día. El sol brilla."
tiempo = tiempo.split()
print(tiempo)

tiempo = "Hace un hermoso día. El sol brilla."
tiempo = tiempo.split(".")
print(tiempo)

tiempo = "Hace un hermoso día. El  sol brilla." # Cuando en esta línea de código haya dos espacios: 
tiempo1 = tiempo.split() # Sin argumento elimina todos los espacios.
tiempo2 = tiempo.split(" ") # Espacio como argumento permite que uno de los espacios no sea borrado.
print(tiempo1)
print(tiempo2)

# Método TITLE: se usa para imprimir en pantalla una palabra o un grupo de palabras con su primer carácter en mayúscula. Ejemplo:
nombre = "danko valderrama"
nombre = nombre.title()
print("Hola {}".format(nombre))

# Método CAPITALIZE: se usa para imprimir en pantalla una palabra o un grupo de palabras, solo con el primer carácter de la frase en mayúscula. Ejemplo:
inicio = "había una vez un enanito"
inicio = inicio.capitalize()
print("{}".format(inicio))

# Método CENTER: se utiliza para centrar un texto dentro de una cantidad específica de carácteres. Ejemplo:
print("Danko".center(13)) # Dentro de 13 carácteres se centrará la palabra Danko.

# Método FORMAT: se usa para imprimir en pantalla outputs con texto y variables de forma distinta a la básica. Para hacerlo escribimos lo siguiente:
a = "perro"
b = "gato"
cantidadLetrasVariableA = len(a)
cantidadLetrasVariableB = len(b)
nombre = "Moisés"
print("Perro tiene {} letras".format(cantidadLetrasVariableA))
# También se pueden agregar dos variables, por ejemplo:
print("Perro tiene {} letras y gato tiene {}.".format(cantidadLetrasVariableA,cantidadLetrasVariableB))
# Y también se pueden colocar en distinto orden agregándole un valor al paréntesis (tomando en cuenta a la primera variable como el valor 0, la segunda el valor 1 y asi sucesivamente):
print("{2} tiene un {0} y un {1}.".format(a,b,nombre))

# El método format también tiene otra aplicación justo dentro de las llaves que se abren para albergar la variable. Haremos un programa para calcular presupuestos:
print()
print("PRESUPUESTO".center(50))
print()
compras = [["Tornillos",723,23.12],["Tuercas",324,4.54],["Arandelas",25,35.63],["Puntas",1430,2.15]]
for i in compras:
    print("{0:12}: {1:8d} x {2:8.2f} = {3:12.1f}".format(i[0],i[1],i[2],i[1]*i[2]))