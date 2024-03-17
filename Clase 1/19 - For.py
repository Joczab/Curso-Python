numbers = [1,2,3,4,5]

for number in numbers :
    if number == 2:
        break
    
    print(number)
    
    print('sssssssssssss')
    
    
for i  in range (1,10):
    print(i)    
    
for i in range(len(numbers)):
    print(i)
    
for index, value in enumerate(numbers):
    print('INDICE', index, 'VALOR', value)
    
else: 
    print('El ciclo ha terminado ')
    
    # Recorre un string

print('Recorre un string')

quote = 'Welcome'

for letter in quote:
    print(letter)

print('-' * 80)

print('Recorrer una lista')

laptop = {
    'model': 'Example-x10',
    'brand': 'Apple',
}

for key in laptop:
    print(f'{key}:{laptop[key]}')
    
print('Recorrer un diccionario')

# Definir una lista que contiene diccionarios
lista_de_diccionarios = [
    {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "María", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Valencia"}
]

# Iterar sobre cada diccionario en la lista
for diccionario in lista_de_diccionarios:
    # Acceder a los elementos del diccionario e imprimirlos
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    print()  # Imprimir una línea en blanco entre cada diccionario

