# funcion que reciba un texto y devuelva el texto invertido

def invertir_texto(texto):
    texto_lista = list(texto)
    texto_lista.reverse()
    
    
    return ''.join(texto_lista)

def invertir_texto_v2(texto):
    return texto[::-1]
    
texto_invertido = invertir_texto('Hola mundo')
print(type(texto_invertido),texto_invertido)

texto_invertido_v2 = invertir_texto_v2('Adios mundo')
print(type(texto_invertido_v2),texto_invertido_v2)

print('------------------------------')

# Funcion para obtener palindromo

def es_palindromo(texto):
    return True if texto.lower() == texto[::-1].lower() else False

print('Es palindromo:', es_palindromo('ReconocEr'))

