set1 = {10,20,30,40,50,50,'john'}
print(type(set1),set1)

print('--------------------------------------------')

# Metodo add (agregar un valor)

set1.add((10,20,20))
set1.add((10,20,20,30))
print(set1)

# Si se ingresa una tupla no se borran los numeros repetidos que fueron agregados a los sets, pero si hay 2 tuplas iguales se elimina 1

print('--------------------------------------------')

# Metodo update ( agrega uno o varios conjuntos mutando el valor)

set1.update({70},{100})
print(set1)

print('--------------------------------------------')

# Metodo discard (elimina un valor)

set1.discard(70)
print(set1)

print('--------------------------------------------')

# Metodo remove (elimina un valor, pero arroja excepcion si este no existe)

set1.remove(10)
print(set1)

print('--------------------------------------------')

# Metodo pop(elimina un valor random)

set1.pop()
print(set1)

print('--------------------------------------------')

# Metodo union (te devuelve un nuevo conjunto a partir de otros)

set_example1 = {80,70}
set_example2 = {'casa', 'pelota'}

set1 = set1.union(set_example1,set_example2)
print(set1)

# Eliminar duplicados de una lista

print('--------------------------------------------')

numbers = [1,1,5,10]

numbers = list(set(numbers))
print(numbers)

# Ejercicio: de dos conjuntos crear uno que muestre los valores en comun

conjunto1 = {1,10,11}
conjunto2 = {10,11,2}

conjunto3 = conjunto1 & conjunto2
print(conjunto3)

# Detiene la ejecucion del programa

exit()