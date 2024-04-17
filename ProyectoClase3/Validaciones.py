''' Funciones para validar'''

def no_vacio(text):
    '''Funcion para validar que no sea vacio el texto'''
    valor = input(text)
    
    while valor.strip() == '' or valor == '':
        print('El valor no puede estar vacio')
        valor = input(text)
        
    return valor

def entero_valido(text, not_text):
    ''' Funcion para validar numeros enteros'''
    valor = no_vacio(text)
    
    while not valor.isdigit():
        print(not_text)
        valor = no_vacio(text)
    
    return valor

def flotante_valido(text, not_text):
        ''' Funcion para validar valore flotantes'''
        
        valor = no_vacio(text).replace(',','.')
        
        while not valor.replace('.','').isdigit():
            print(not_text)
            valor = no_vacio(text)
            
        while float(valor) < 0.0:
            print('El saldo inicial debe ser mayor a 0.\n')
            valor = no_vacio(text)
    
        return format(float(valor),'.2f')

def finalizar():
    return print('\nFinalizado.\n')

def mostrar_menu(opciones: list):
    '''Funcion de mostrar menu'''
    
    opciones = [(f'Para {opcion['accion']}:{opcion['valor']}') for opcion in opciones]
    
    for opcion in opciones: 
        print(opcion)        
        
def validar_opcion(opciones: list):
    ''' Funcion para validar las opciones'''
    opcion_selec = entero_valido('Que desea seleccionar?:\n', 'La opcion seleccionada debe ser un numero.\n')
    
    while(len([opcion for opcion in opciones if opcion['valor'] == opcion_selec])==0):
        print('La opcion seleccionada no se encuentra dentro de las disponibles.\n')
        opcion_selec = entero_valido('Que desea seleccionar?:\n', 'La opcion seleccionada debe ser un numero.\n')
    
    return int(opcion_selec)    
