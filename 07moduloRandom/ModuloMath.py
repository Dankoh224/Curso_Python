# Existen diversos módulos que no están cargados en la memoria de Python. Esto se debe a que no es necesario usar más espacio en memoria si no se van a usar estos recursos. Para llamar estos recursos usaremos la palabra reservada "import". Ejemplo:
import math
# Para ver los recursos que contiene este módulo usamos el comando dir():
print(dir(math))
# Para usar, por ejemplo, el comando raíz cuadrada, escribimos el módulo math seguido de un punto y el comando a utilizar. Ejemplo: 
print(math.sqrt(9))
# IMPORTANTE: en internet existen miles de páginas que explican para que sirve cada uno de los comandos del módulo math.

# Otro recurso que tiene este fichero o módulo, es que podemos importar solo lo que necesitemos de él, por ejemplo, si solo necesitamos el valor de pi y la función de raíz cuadrada escribimos:
from math import pi, sqrt

