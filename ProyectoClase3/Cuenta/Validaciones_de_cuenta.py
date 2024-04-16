import random
from Validaciones import entero_valido, flotante_valido

def random_acount_number():
    """funcion de numero aleatorio de cuenta"""
    minimo = 10 ** (12 - 1)
    maximo = 10**12 - 1
    return random.randint(minimo, maximo)


def valid_account():
    """Funcion de Numero de cuenta"""
    cuenta = entero_valido('Numero de cuenta del usuario:\n','El numero de cuenta debe ser un entero.\n')
    return int(cuenta)
    
def saldo_inicial(text):
    """ Funcion de Saldo inicial"""
    saldo = flotante_valido(text,'El saldo inicial debe ser un numero.\n')
    return float(saldo)
