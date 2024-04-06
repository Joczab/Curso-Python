def saludos(bienvenida,**kwargs):
    print(bienvenida)
    print(kwargs)
    
    
    for key,value in kwargs.items():
        print(f'{key} = {value}')
    
saludos('Bienvenido/a ',name = 'Jose', lastname = 'Zabala', age = 21)
