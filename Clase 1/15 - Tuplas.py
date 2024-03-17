numbers = (1 , 2 , 3 , 4 , 5 )

print (type(numbers))
print (numbers)

# index

index = numbers.index(2)

print ("POSICION", index)
print('VALOR A TRAVES DE LA POSICION',numbers[index])

# count

x = numbers.count(5)
print(f'Ocurrencias "S": {x}')