# Define una función que tome como parámetro un número y devuelve el triple del doble de ese número. Llama la función y pásale como argumento un número que pidas al usuario. Muestra el resultado por pantalla.

def tripleDelDoble (numero):
    resultado = 3*2*numero
    return resultado

x = float(input("Ingrese un número: "))
print(tripleDelDoble(x))

# NOTA: si la función la escribimos con un print en vez de un return, se imprime inmediatamente al llamar a la función:

def DobleDelTriple (numero):
    resultado = 3*2*numero
    print(resultado)

x = float(input("Ingrese un número: "))
DobleDelTriple(x)