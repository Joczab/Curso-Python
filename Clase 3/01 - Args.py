def imprimir_numeros(*args):
    
    print(args)
    for item in args:
        print(item)
    
    
imprimir_numeros(10,20,30,40,50,'holamundo')

# con propiedades(numero)

def sumar_numeros(numero,*args):
    '''Los args son numeros'''
    
    for item in args:
        print(item + numero)    
        
sumar_numeros(5,10,11,20,1000)
