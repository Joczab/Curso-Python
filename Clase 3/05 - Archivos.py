path = './clase 3/text.txt'

file = open(path, 'a+', encoding='utf-8')

# lee todo el archivo
file.write('Hello')

file.close()

file = open(path, 'r', encoding='utf-8')

#lee todo el archivo

print(file.read())

# lee linea por linea

'''print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())'''

# leer linea por liea con for loop
for line in file:
    print (line)
    
# numbers = list(iter(range(5)))
numbers = iter((1,2,3))

'''print(next(numbers))
print(next(numbers))
print(next(numbers))'''

# with eb archivos

with open(path, 'r',encoding = 'utf-8') as file:    
    print('Usando open ',file.read())

