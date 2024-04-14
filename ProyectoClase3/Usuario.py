from ProyectoClase3.Persona import Persona

class Usuario(Persona):
    
    def __init__(self,name,lastname,cedula,password,cuentas):
        
        super().__init__(name,lastname,cedula)
        self.password = password
        self.cuentas = cuentas
        
    
    