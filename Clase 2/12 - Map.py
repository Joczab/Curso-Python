usuarios = [
    {
        'username': 'fulano 1',
        'active': False
    },
    {
        'username': 'fulano 2',
        'active' : False
    }
]
print(usuarios)
def cambio_status(usuario):
    usuario['active'] = True
    return usuario

# map sin lambda

nuevo_statu = map(cambio_status,usuarios)

print('V1',list(nuevo_statu))

print('-----------------------------------------------------------------------')

# map con lambda

nuevo_statu_v2 = map(lambda usuario: {**usuario,'active':False},usuarios)
print('V2',list(nuevo_statu_v2))

print('-----------------------------------------------------------------------')

# iterar varias listas con map

numbers1 = list(range(0,5))
numbers2 = list(range(5,10))
print(numbers1)
print(numbers2)

numbers3 = list(map(lambda x, y: x + y, numbers1, numbers2))

print(numbers3)
