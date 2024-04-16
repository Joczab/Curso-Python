from SistemaBancario import SistemaBancario
from Usuario.Usuario import Usuario
from Cuenta import Cuenta

def app():
    '''Inicializar applicacion'''
    
    usuario_1 = Usuario(
        nombre="John",
        apellido="Doe",
        cedula=26275576,
        username="johndoe",
        password="123456",
        cuentas=[Cuenta(account_id=123456789101, saldo=400.00)],
    )
    
    usuario_2 = Usuario(      
        nombre="Ryan",
        apellido="Smith",
        cedula=25645888,
        username="ryansmith",
        password="123456",
        cuentas=[Cuenta(account_id=123456789102, saldo=400.00)],
    )
    
    SistemaBancario([usuario_1,usuario_2]).main()
    
    if __name__ == '__main__':
        app()