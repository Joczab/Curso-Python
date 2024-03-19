numbers = [1,2,3,4]
print(type(numbers))

# Leer
print (f'PRIMERA POSICION {numbers[0]}')

# Update 

numbers[len(numbers) - 1] = 5
print(numbers)

# Eliminar

del numbers[2]
print(numbers)

# Cortes

# print (numbers[posicion comenzando de 0: posicion de longitud])
print (numbers[0:3])
