#Si quiero saludar 3 veces a distintas personas, debo escribir:
print("Hola, como estás?")
print("Hola, como estás?")
print("Hola, como estás?")
#Pero si quiero evitar esto puedo usar funciones de la siguiente manera:
def saludar():
    print("Hola, como estás?")
#Luego, para que se ejecute lo que está dentro de la función saludar, solo debo llamar a la función:
saludar()

#Existe otra forma de escribir las funciones, cuando fijamos un parámetro dentro del paréntesis.
#Hacemos esto para que al darle un ARGUMENTO a la función, la función retorne un resultado.
#Ejemplo:

def fcuadrada (num):
    resultado = num**2+3*num-1
    return resultado
#Sin embargo, al usar las funciones de esta otra forma, NO se imprime el resultado al llamar
#a la función como lo hicimos en un inicio, ya que la variable resultado esta definida solo de 
# manera local, es decir, solo existe dentro de esa función:
fcuadrada(4)
#Por lo que es necesario imprimir con el comando print, este llamado:
print(fcuadrada(4))

#Otra forma de escribir eficientemente, es indicándole a return, que es lo que queremos hacer
#con el parámetro de la función:
def fraizcuadrada (num):
    return num**(1/2)
print(fraizcuadrada(81))

#FUNCIÓN CON PARÁMETROS MÚLTIPLES: Una función puede definirse con uno o más parámetros de una
#forma muy sencilla y parecida a la anteriormente descrita. Ejemplo:
def sustracciones (minuendo,sustraendo,veces):
    return minuendo - sustraendo * veces
print(sustracciones(22,3,4))

#FUNCIONES QUE NO DEVUELVEN NADA: son funciones que en vez de devolver un valor,
#devuelven un procedimiento. En Python, todas las funciones devuelven algo y las
#que no devuelven nada van a devolver el valor NON. Como ejemplo haremos una
#pantalla de inicio:
def pantallaDeInicio ():
    print("*******************************")
    print("*                             *")
    print("*    PANTALLA DE INICIO       *")
    print("*                             *")
    print("*   Bienvenido al Sistema     *")
    print("*                             *")
    print("*******************************")
    return None
#si en este momento escribo return None (como se ve en la línea anterior) o si
#no escribo nada, se dará exactamente el mismo caso: devolvera el valor "None"
#al imprimir la función.
print(pantallaDeInicio())

# FUNCIONES QUE DEVUELVEN VERDADERO Y FALSO: En ocasiones, una función nos servirá
# para trabajar con condiciones y bucles. Si queremos que nuestra función
# condicione alguna situación, haremos lo siguiente:
def numeroPar (numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(numeroPar(8))
# Es importante notar, para acortar código, que también puede escribirse de la 
# siguiente forma:
def numeroPar (numero):
    if numero % 2 == 0:
        return True
    return False
# Esto es posible (que al entrar al if no continúe con el siguiente return),
# ya que python termina inmediatamente de leer una función si retorna algo.
# Por último, si usamos un if else, podemos decir si es par o no es par:
numero = 8
if numeroPar (numero):
    print("Es par.")
else:
    print("No es par.")

# COMANDO PASS: este comando nos permite escribir mi función sin que esta este 
# finalizada, es decir, es un boquejo a omitir por Python:
def pesos ():
    perro
    pass

# FUNCIONES QUE DEVUELVEN VARIOS VALORES:
# En este caso podemos devolver con return varios valores con el ingreso de una 
# sola variable. Para devolver los valores lo haremos dentro de una tupla:
def valores (n):
    return 2*n, 3*n, 2**n, n**2
print(valores(5))
# También podemos devolver un grupo de valores dentro de unas variables:
def valoresDentroDeVariables (n):
    return 3*n,3+4*n,n-6
a,b,c = valoresDentroDeVariables(2)
print(a,b,c)

# OBJETOS MUTABLES COMO ARGUMENTOS DE UNA FUNCIÓN.
# Cuando trabajamos con argumentos mutables, como listas, debemos tener cierto
# cuidado para evitar que nuestra función, cambie los valores de la lista original.
# ejemplo: Obtener las mejores 2 notas del grupo.
def mejoresNotas (lista):
    lista.sort()
    return lista[2:4]
lista = [5,4,7,6]
print(lista)
print(mejoresNotas(lista))
print(lista)
# El problema de hacerlo así es que la lista será cambiada por nuestra función. Por
# lo tanto, realizaremos el siguiente truco. Ejemplo: obtener las 3 notas más bajas
lista = [6,4,6,8,4,5,3,2]
print(lista)
def notasMasBajas ():
    copiaLista = list(lista)
    copiaLista.sort()
    return copiaLista[0:3]
print(notasMasBajas())
print(lista)




