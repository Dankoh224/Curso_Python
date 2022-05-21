import sys
intervalo = range(1,101)
print(intervalo)

intervalo2 = list(range(1,101))
print(intervalo2)

bytesEnMemoriaIntervalo1 = sys.getsizeof(intervalo)
bytesEnMemoriaIntervalo2 = sys.getsizeof(intervalo2)
print(bytesEnMemoriaIntervalo1)
print(bytesEnMemoriaIntervalo2)