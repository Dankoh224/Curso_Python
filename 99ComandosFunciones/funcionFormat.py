#La función ".format()" es muy útil para ordenar los datos de salida de nuestras
#aplicaciones. Suponiendo que se quiere dar como salida de tu programa una
#tabla con los resultados ordenados. Ejemplo:
nombre = "Danko"
apellido = "Valderrama"
print("Hola {}, ¿como estás?".format(nombre))
#Además, la función format soporta mas de una sola variable, por ejemplo:
a = int(input("Ingrese la constante a: "))
b = int(input("Ingrese la constante b: "))
c = int(input("Ingrese la constante c: "))
print("El número {0} es el factor de x^2, {1} es el factor de x y {2} la constante.".format(a,b,c))

#Por último, también podemos usar los números de las posiciones en las que se va
#a insertar el argumento. Esto nos da la posibilidad de repetir alguna variable 
#en un espacio determinado. Como por ejemplo:
a = 12
b = 13
c = 15
print("Ana obtuvo {0}, Sergio {1} y Camila {2}. Manuel tambien obtuvo {1}".format(a,b,c))
#Ejemplo 2
a = "abra"
b = "cad"
print("¡¡¡{0}{1}{0}!!!".format(a,b))

# También se puede realizar de otra forma, que en realidad es solo transformar el 
# interior del print en una variable, y luego imprimir la
# variable.format(argumento1,argumento2,...) PIDIENDO LOS ARGUMENTOS AL FINAL.
text = "SU nombre es {name} {lastname}, a que sí, lo sé, lo he adivinado con mis super poderes poderosos."
print(text.format(name=input("Ingrese nombre: "), lastname=input("Ingrese apellido: ")))
