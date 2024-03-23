# importamos reduce
from functools import reduce
import operator
numbers = list(range(0,10))

# sumar todos los numeros de la lista con la posicion reduce(con lambda)

sumatoria = reduce(lambda x, y : x + y, numbers)
print(sumatoria)

# sumatoria con operator

sumatoria2 = reduce(operator.add, numbers)
print('Sumatoria con operator add:', sumatoria2)

# mayor numero

numbers1=[1,100,20,40,2,1]

mayor_numero = reduce(lambda x, y: x if x > y else y, numbers1)

print('Mayor numero: ',mayor_numero)

# menor numero

menor_numero = reduce(lambda x, y: x if x < y else y, numbers1)

print('Menor numero: ',menor_numero)

print('--------------------------------------------------------------------')
print('usando la funcion max()', max(numbers1))
print('usando la funcion min()', min(numbers1))


