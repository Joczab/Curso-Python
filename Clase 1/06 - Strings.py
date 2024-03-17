# Forma de concatenar

text1 = 'text1'
text2 = "text2"

# Forma 1

output = text1 +" "+ text2
print(output)

# Forma 2

welcome = 'Bienvenido a {}, estudiante {} '.format("URBE","JUAN")
print(welcome)

# Forma 3

place = "URBE"
name = "JUAN"
year = 1998
welcome = f'Bienvenido a {place}, estudiante {name} ,{year}'
print(welcome)

# Tipos de formatting

price = 40
quote = f'el precio fue de {price + 2 :.2f}$'
print(quote)

