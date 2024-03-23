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

