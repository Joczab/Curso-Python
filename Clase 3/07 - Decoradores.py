#asignar funciones a variables

def suma(x, y):
    return x + y

#instanciamos funcion en variable

sumar = suma

print(sumar(10,20))

# funcion dentro de otra

def anadir_uno(numero):
    
    def anadir(numero): 
        return numero + 1
    
    resultado = anadir(numero)
    
    return resultado

print(anadir_uno(5))

# funciones como parametros de otra funcion

def sumar_2(x,y):
    return x + y
def calculadora(operacion, x, y):
    return operacion(x,y)

print(calculadora(sumar_2,10,20))    

def imprimir_mensaje(mensaje):
    
    def imprimir():
        return mensaje
    return imprimir()

print(imprimir_mensaje('Este es un mensaje'))

# funciones que devuelven funciones

def upper_split(text):
    text = text.upper()
    
    def to_split():
        return text.split()
    
    return to_split

upper_text = upper_split('Hello python')
split_text = upper_text()

print(split_text)

# decoradores


def uppercase_decorador(function):
    
    def wrapper():
        valor = function()
        return valor.upper()
        
    return wrapper

def split_decorador(function):
    
    def wrapper():
        valor = function()
        return valor.split()
        
    return wrapper

@split_decorador
@uppercase_decorador
def texto():
    return 'Esto es un texto'

# primera forma de ejectuar un decorador
#decorador = uppercase_decorador(texto)
#print(decorador())
# print(uppercase_decorador(texto))
print(texto())


# decoradores con argumentos

def decorador_username(function):
    def wrapper(req, res):
        req['body']['username'] = 'max'
    return wrapper

req = {
    'body' : {
        'username': 'john',
        'password': '123456'
    }    
}
@decorador_username
def main(req, res):
    print(req)

main(req, res={})