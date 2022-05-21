#Listas y Tuplas.

#Las listas en Python son:
#Heterogéneas: pueden estar conformadas por elementos de distintos tipo, incluidos otras listas.
#Mutables: sus elementos pueden modificarse.

#Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos.

L = ["almacenar",8,"a",[1,2,3],True,(0,0,1),85.7,(0,0,1),8]


#1) POSICIÓN dado un elemento de la lista: ---> L.index(elemento)
#Guarda en una variable la posición que obtienes para  imprimirla:
#(La posición comienza en 0)

print("1) ",L.index((0,0,1)))

#2) ELEMENTO dada la posición de la lista: ---> L[número posición]

print("2) ",L[2])

#3) ELEMENTO dada la posición NEGATIVA de la lista: ---> L[número NEGATIVO posición]

print("3) ",L[-2])

#4) IMPRIMIR todos los elementos (o recorrer) con un ciclo FOR:

print("4) ")
for i in L:
    print(i)

#5) CAMBIAR TODOS los elementos de una lista NUMÉRICA con un ciclo FOR:

M = [1,2,3,4,5]
print("5) ")
print(M)
for i in range(len(M)):
    M[i]= M[i] + 5
print(M)

#6) IMPRIMIR un TROZO de lista:
print("6)")

print("Imprimir de 2 a 4 (no cuenta el 4):")
print(M[2:4])
print("Imprimir del principio a 4 (no cuenta el 4):")
print(M[:4])
print("Imprimir del 2 hasta el final (si cuenta el último número):")
print(M[2:])
print("Queda igual sin números:")
print(M[2:4])

#7) CAMBIAR un elemento por otro nuevo: ---> L[número posición] = elemento nuevo
print("7) ")
L[2] = "elemento nuevo"
print(L)

#8) CAMBIAR un TROZO de lista:

print("8)")
L[3:5] = ["perro","gato"]
print(L)

#INSERTAR EN UNA LISTA

#9) INSERTAR elemento en una posición definida: ---> L.insert(posición a usar,número a insertar)
print("9)")
L.insert(1,"pálpito")
print(L)

#10) AGREGAR elemento al final de una lista: ---> L.append(numero)
print("10)")
L.append(45)
print(L)

#11) AGREGAR más de un elemento al final de la lista (si se usa una cadena de texto ingresará cada carácter uno a uno. si se agrega una variable númerica no agregará nada y dará error ya que no agrega de a un número, para eso es append): ---> L.extend(lista2)
print("11)")
M = [1,2]
L.extend(M)
print(L)

#ORDENAR EN UNA LISTA
#12) MENOR A MAYOR: ---> L.sort()
print("12)")
L=[10,4,6,8,3,5,7,2,9,1]
print(L)
L.sort()
print(L)

L = ["afg","cfc","bnj","fgf","dhu","eid"]
print(L)
L.sort()
print(L)

#13) MAYOR A MENOR: ---> 1º L.sort(), luego L.reverse()
print("13)")
L=[10,4,6,8,3,5,7,2,9,1]
print(L)
L.sort()
L.reverse()
print(L)

L = ["afg","cfc","bnj","fgf","dhu","eid"]
print(L)
L.sort()
L.reverse()
print(L)

#14) INVERTIR una lista: L.reverse()
print("14)")
L = [1,5,3,4,5,2]
print(L)
L.reverse()
print(L)

#ELIMINAR ELEMENTOS:
#15) BORRAR elemento dado ELEMENTO (borra solo la primera coincidencia): ---> L.remove()
print("15)")
print(L)
L.remove(5)
print(L)

#16) BORRAR ELEMENTO dado ELEMENTO (borra todas las coincidencias):
print("16)")
L = [2,5,4,3,5,8,7,5,3,5]
print(L)
for x in L:
    if x == 5:
        L.remove(5)
print(L)

#17) BORRAR elemento dada POSICIÓN: ---> del L[posición]
print("17)")
print(L)
del L[3]
print(L)

#18) BORRAR elemento dada POSICIÓN: ---> L.pop(posición)
print("18)")
print(L)
L.pop(2)
print(L)

#19) BORRAR último elemento de una lista: --->L.pop()
print("19)")
print(L)
L.pop()
print(L)

#20) BORRAR varios elementos: del L[inicio:fin]
print("20)")
L = [3,2,4,3,2,4,3,2,2,4,3]
print(L)
del L[3:7]
print(L)

#21) BORRAR todos los elementos de una lista: ---> L.clear()
print("21)")
L.clear()
print(L)

#21) CONTAR cuántas veces aparece un elemento en una lista: ---> L.count(2)
print("21)")
L = [3,2,4,3,2,4,3,2,2,4,3]
print(L)
x = L.count(2)
print(x)

#22) CONTAR la cantidad de elementos de una lista: ---> len(L)
print("22)")
print(len(L))

#23) HALLAR EL MINIMO: min(L)
print("23)")
print(min(L))

#24) HALLAR EL MAXIMO: max(L)
print("24)")
print(max(L))

#25) SUMA de los elementos: sum(L)
print("25)")
print(L)
print(sum(L))

#26) COMPARAR LISTAS:
print("26)")
if M == L:
    print("Coincide.")
else:
    print("Sin coincidencia.")

#OPERACIONES MATEMÁTICAS EN LAS LISTAS.
    
#27) COMBINAR LISTAS USANDO (+):
print("27)")
print(L)
print(M)
print(L+M)

#28) DUPLICAR O TRIPLICAR LISTAS USANDO (*):
print("28)")
print(L)
print(L*2)

#29) TRANSFORMAR una CADENA (palabra) en una lista con carácteres separados: ---> list(str)
print("29)")
L = "PERRITO Y PERROTO"
print(L)
L = list(L)
print(L)

#30) SEPARAR una CADENA en una lista separando palabras: ---> split()
print("30)")
r = "PERRITO Y PERROTO"
print(r)
L = r.split()
print(L)

#31) SEPARAR CADENA en una lista separada en palabras: --->split(,)
print("31)")
r = "Hola,cauros,como,estan. Podrían,venir,pa,la,casa? Chaulin"
print(r)
L = r.split(",")
print(L)

#32) UNIR lista en una cadena: ---> separador.join(L)
print("32)")
print(L)
separador = " "
print(separador.join(L))
print(L)

#33) ALISING: el objeto tiene más de una referencia con más de un nombre (listas mutables):
print("33)")
L = [1,2,3,4,5,6]
m = L
m[2] = "caracaracho"
print(L)
"""En este caso, al cambiar el valor de la segunda lista, cambia también el de la lista original. Si no quieres
que cambie el valor para la original debes usar la función L.copy()"""
s = L.copy()
s[2] = "perrito"
print(L)

#34) CREAR LISTA que CUENTE cantidad de elementos.
print("34)")
H = []
L = ["almacenar",8,"a",[1,2,3],True,(0,0,1),85.7,(0,0,1),8]
for i in L:
    frecuencia = L.count(i)
    if frecuencia == 1:
        H.append((i,frecuencia))
    else:
        H.append((i,frecuencia))
        while frecuencia != 0:
            del L[L.index(i)]
            frecuencia = frecuencia - 1

#35) INDICES NEGATIVOS:
print("35)")

print(L)
print(L[0])
print(L[1])
print(L[2])
print(L[-1])
print(L[-2])
print(L[-3])
print(L[-4])
print(L[-5])

#36) RANGO con saltos de n en n: ---> L[inicio,de cuanto en cuanto]
print("36)")
L = L*3
print(L)
l5 = L[1::1]
print (l5)

l5 = L[1::2]
print (l5)

l5 = L[1::3]
print (l5)

l5 = L[1::4]
print (l5)

l5 = L[1::6]
print (l5)

#37) JUNTAR EN DUPLAS dos listas: ---> zip(Lista1,Lista2)
print("37)")
puesto = [1,2,3]
premio = ["100.000 mil pesos.","50.000 mil pesos.","10.000 pesos."]

posiciones = zip(puesto, premio)

for i in posiciones:
    print(i)

#38) CREAR ORACIONES CON elementos combinados.
print("38)")
puesto = [1,2,3]
premio = ["100.000 mil pesos.","50.000 mil pesos.","10.000 pesos."]

posiciones = zip(puesto, premio)
for pu, pre in posiciones:
    print("Si llegas en la posición ",pu," ganarás ",pre)

#39) CREAR LISTA con elementos combinados: ---
print("39)")
puesto = [1,2,3]
premio = ["100.000 mil pesos.","50.000 mil pesos.","10.000 pesos."]

posiciones = list(zip(puesto, premio))
print(posiciones)

    
