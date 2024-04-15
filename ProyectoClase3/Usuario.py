from ProyectoClase3.Persona import Persona
from ProyectoClase3.Cuenta import Cuentas

class Usuario(Persona):
    
    def __init__(self,name,lastname,cedula,nombre_usuario,password):
        
        super().__init__(name,lastname,cedula)
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.cuentas = []
        
    def crear_cuenta_bancaria(self,num_cuenta,saldo):
        if not any(cuenta.num_cuenta == num_cuenta for cuenta in self.cuentas):
            nueva_cuenta = Cuentas(num_cuenta,saldo)
            self.cuentas.append(nueva_cuenta)
            print('Se ha creado correctamente.\n')
        else:
            print('Ya posee una cuenta bancaria.\n')
    
    