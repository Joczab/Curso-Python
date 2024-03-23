usuarios = [
    {
        'username': 'username 1',
        'status': True
    },
    {
        'username': 'username 2',
        'status': False
    },
    {
        'username': 'username 3',
        'status': True
    }
]

usuarios_inactivos = list(filter(lambda usuario: True if usuario['status'] == False else False,usuarios))
print(usuarios_inactivos)

