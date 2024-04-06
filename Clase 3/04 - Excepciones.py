#Asserts

def suma(x, y) : return x + y

#explota
assert suma(10,10) == 20, 'Hubo un error'

# Exception

try: 
    name = 'Jose'
    
    if name != 'Daniel':
        raise Exception('Nombre incorrecto')
        
    #print('hola mundo' + 10 )
    # raise Exception('Esto es un error')
except Exception as e:
    print (e)
    print(type(e))

except SyntaxError as s:
    print(s)

print('hello')

print('------------------------------------------------\n')

numbers = range(5)
try:
    print(numbers[10])
except IndexError as ie:
    print('IndexError ->', ie)
except Exception as e:
    print('Excepcion general ->', e)

print('---------------------------------------------------\n')

try:
    int('1')
except ValueError as ie:
    print('ValueError ->',ie)
except Exception as e :
    print('Excepcion General ->' , e)
finally:
    print('Se ejecuta de todos modos.\n')
    