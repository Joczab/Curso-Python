from SistemaBancario import SistemaBancario
from Usuario.Usuario import Usuario
from Cuenta.Cuenta import Cuenta

def app():
    '''Inicializar applicacion'''
    
    usuario_1 = Usuario(
        name ="John",
        lastname ="Doe",
        cedula=26275576,
        username="johndoe",
        contraseña="123456",
        cuentas=[Cuenta(account_id=123456789101, saldo=400.00)],
    )
    
    usuario_2 = Usuario(      
        name="Ryan",
        lastname="Smith",
        cedula=25645888,
        username="ryansmith",
        contraseña="123456",
        cuentas=[Cuenta(account_id=123456789102, saldo=400.00)],
    )
    
    SistemaBancario([usuario_1,usuario_2]).main()
    
if __name__ == '__main__':
     app()