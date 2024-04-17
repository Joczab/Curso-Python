class Persona:

    def __init__(self,nombre,apellido,cedula)-> None:
        
        self.nombre = nombre 
        self.apellido = apellido
        self.cedula = cedula

    def set_nombre(self,nuevo_nombre):
        '''Set nombre'''
        self.nombre = nuevo_nombre        
    
    def set_apellido(self,nuevo_apellido):
        '''Set apellido'''
        self.apellido = nuevo_apellido  
    
    def set_cedula(self,nueva_cedula):
        '''Set cedula'''
        self.cedula = nueva_cedula        
    