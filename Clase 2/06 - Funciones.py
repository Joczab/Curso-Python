import random

def saludos ():
#    print( 'hola mundo' )
 return'saludos'
print(saludos())

print('------------------------------')

def add(x,y):
    return x + y

print(add(10,20))

# instanciar funcion en variable sin llamar

instanciar = add

# llamando a la funcion con el nuevo nombre

print(instanciar(10,30))

# Funcion de multiple return

user = {
    'name' : 'Leonardo',
    'lastname': 'Villalobos',
    'active': True 
}

def get_user_data(user):
    
    name = user['name']
    is_active = user['active']
    
    return name , is_active


result1 = get_user_data(user)

print(type(result1),result1)

print('name', result1[0])
print('active', result1[1])

print('------------------------------')

randon_num =random.randint(0,10)
print(randon_num)

def random_number(x = 0,y= 1000):
    return random.randint(x,y)

random_value = random_number()

print(random_value)

