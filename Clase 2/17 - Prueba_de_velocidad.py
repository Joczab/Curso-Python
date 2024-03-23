from math import sqrt
from time import time

start_time = time()

numeros = list(range(0,10000))

print(numeros)

# compresion de listas

def raiz(numero):
        return sqrt(numero)

compresion = [raiz(numero) for numero in numeros]
print(compresion)


'''compresion = map(lambda x: sqrt(x), numeros)
print(list(compresion))'''


end_time = time()

tiempo = end_time-start_time
print(tiempo)


# sqrt 0.03847861289978027
# map 0.04152989387512207 (el map es mas lento que el sqrt si se pasa un lambda, pero normalmente es el mas rapido)