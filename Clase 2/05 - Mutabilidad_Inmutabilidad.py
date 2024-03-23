# string (no es mutable)
text = 'Bienvenido al curso '
text = text + 'python'
print (text)


# estamos mutando (arroja error)
# text[0] = 'b'

# estamos creando un nuevo valor (no mutando)
text = text.replace('B', 'b')
print(text)

# number (los tipos de numeros no se puede mutar)

'''number = 10
print(number[0])'''

# tupla(no se puede mutar)
tupla = tuple(range(0,10))
print('Tupla:', tupla)

#tupla[0]=1 (no se puede mutar)

# lista

numbers = list(range(0,10))

print('Longitud: ', len(numbers), 'Resultado: ', numbers)

# estamos mutando la lista

numbers[0] = -1
print(numbers)

# mutamos cuando agregamos un solo valor

numbers.append(10)

print(numbers)

# spread para no mutar (lo usamos para a;adir varios valores)

numbers = [*numbers,11,12,13, *[14,15,16]]
print(numbers)

print('------------------------------')

# diccionarios

curso = {
    'titulo' : 'Python',
    'seccion' : 'N-103'
}
print(curso)
# mutar diccionario

curso['numero_alumnos'] = 12

print('mutando: ',curso)

# no mutar con spread (creamos un nuevo diccionario)

curso1 = {**curso,'profesor': 'Ronald'}
print(curso1)