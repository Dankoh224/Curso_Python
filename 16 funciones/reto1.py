# Define una función que tome como parámetro un número y devuelve el triple del doble de ese número. Llama la función y pásale como argumento un número que pidas al usuario. Muestra el resultado por pantalla.

def tripleDelDoble (numero):
    resultado = 3*2*numero
    return resultado

x = tripleDelDoble(float(input("Ingrese un número: ")))

print(x)