# Existen diversos módulos que no están cargados en la memoria de Python. Esto se debe a que no es necesario usar más espacio en memoria si no se van a usar estos recursos. Para llamar estos recursos usaremos la palabra reservada "import". Ejemplo:
import random
# Para ver los recursos que contiene este módulo usamos el comando dir():
print(dir(random))

# Los comandos que veremos a continuación son: "randint", "choice" y "shuffle".
# Comando RANDINT: Obtienes un número al azar entre los valores del argumento incluyéndolos.
print(random.randint(1,10))
# Comando CHOICE: Obtienes un valor al azar de entre una selección de valores que has incluido, no necesariamente, números, ni tampoco, dentro de un rango. Ejemplo:
print(random.choice([4,"a",8,True]))

# Comando SHUFFLE: Esta función baraja los elementos de una lista, ordenandolos sin ningún orden. Ejemplo:
lista = [1,2,3,4,5]
random.shuffle(lista)
print(lista)

# Comando SAMPLE: Esta función nos dará una lista con n elementos de otra lista. Ejemplo:
lista1 = ["perro",3,"m",True,False,3+2j]
lista2 = random.sample(lista1,3) # En el alrgumento se escribe la lista madre y la cantidad de elementos que se quieren sacar aleatoriamente. 
print(lista1)
print(lista2)