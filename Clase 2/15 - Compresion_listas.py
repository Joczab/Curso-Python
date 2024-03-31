numbers = list(range(0,10))

# filtrar numeros impares con compresion de listas

impares = [numero for numero in numbers if numero % 2 != 0]

print(impares)

paises = ['veneZuela', 'ChiLe', 'Colombia']
print(paises)
paises_formateados = ['Maracaibo' if pais.capitalize() == 'Venezuela' else pais.capitalize() for pais in paises]

print(paises_formateados)

