# funciones puras

def cuadrado (num):
    return num ** 2

print(cuadrado(3))

# funciones impuras

clientes = ['ronald', 'esteban','leonardo'] 

def agregar_cliente (nombre):
    #inserto nuevo cliente
    clientes.append(nombre)
    # retorno el valor
    return clientes
    
    
result1 = agregar_cliente('jose')

print(result1)

result2 = agregar_cliente('davi')

print(result2)

