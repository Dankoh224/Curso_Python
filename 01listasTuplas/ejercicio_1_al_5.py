#ejercicio 1: solicitar al usuario que ingrese números, los cuales se guardaran en una lista. Finalizar al ingresar
#el número cero, el cual no debe guardarse.

numeros = float(input("Ingrese número: "))
L = []
while numeros != 0:
    L.append(numeros)
    numeros = float(input("Ingrese número: "))
print(L)

#ejercicio 2: a continuación, solicitar al usuario que ingrese un número y, si el número esta en la lista, eliminar
#su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

x = float(input("Ingrese un número"))
contador = 0
for i in L:
    if i != x:
        contador = contador + 1
        if contador == len(L):
            print("No hay ocurrencia. No hay nada que eliminar")
            break
    else:
        ocurrencia = L.index(i)
        del L[ocurrencia]
        print("Eliminada primera ocurrencia.")
        print("La nueva lista es: ",L)
        break

#ejercicio 3: Imprimir la sumatoria de todos los números de la lista.
sumatoria = 0
for i in L:
    sumatoria = sumatoria + i
print("Suma:",sumatoria)

#ejercicio 4: Solicitar al usurio otro número y crear una lista con los elementos de la lista original que sean menores
#que el número dado. Imprimir esta nueva lista, iterando por ella.
G = []
x = float(input("Ingrese UN número para crear la nueva lista: "))
for i in L:
    if i < x:
        G.append(i)
print(G)

#ejercicio 5: Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta  por un
#número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es
#[5,16,2,5,57,5,2] la nueva lista contendrá: [(5,2),(16,1),(2,2),(57,1)].
H = []
for i in L:
    rep = L.count(i)
    if rep == 1:
        H.append((i,rep))
    else:
        H.append((i,rep))
        while rep != 0:
            del L[L.index(i)]
            rep = rep - 1
print(L)
print(H)