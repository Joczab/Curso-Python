from Persona import Persona
from Cuenta.Cuenta import Cuenta

class Usuario(Persona):
    
    _contraseña = None
    
    def __init__(self, name, lastname, cedula, username,contraseña,cuentas: list[Cuenta] = None):
        super().__init__(name, lastname, cedula)
        self.username = username
        self._contraseña = contraseña
        self.cuentas = cuentas
    
    def set_username(self, nuevo_username):
        '''Set nombre de usuario'''
        self.username = nuevo_username
        
    def set_contraseña(self, nueva_contraseña):
        '''Set contrasena'''
        self._contraseña = nueva_contraseña
        
    def set_cuentas(self, nueva_cuentas: list[Cuenta]):
        '''Set nombre de usuario'''
        self.cuentas = nueva_cuentas
        
    def validar_contraseña(self, contraseña):
        '''validar contraseña'''
        return self._contraseña == contraseña
        
        