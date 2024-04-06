from uuid import uuid1

class Persona:
    
    _bank_account = uuid1()
    
    
    # El contructor __init__ se va a ejecutar al instanciar la clase
    def __init__(self, name, lastname):
        # estamos creando atributos
        self.name = name
        self.lastname = lastname
        
        
persona1 =  Persona('Jose','Zabala')
print(f'Persona 1 : {persona1.name} {persona1.lastname} {persona1._bank_account}')

persona2 =  Persona('Jesus','Zabala')
print(f'Persona 2 : {persona2.name} {persona2.lastname}')

class Estudiante(Persona):
    
    
    __code = uuid1()
    
    def __init__(self, name, lastname):
        #heredamos los atributos de persona
        super().__init__(name, lastname)
        
        # estudiar en privado (llamar metodo privado)
        self.__estudiar()
    
    def hablar(self):
        print('Hablar')

    def __estudiar(self):
        print('estudiando en privado')
        
    @staticmethod 
    def sumar(a,b):
        return a + b
        
    #getter
    
    def get_code(self):
        return self.__code    
    
    #Setter
    
    def set_code(self, code):
        self.__code = code
        
Estudiante1 = Estudiante('Maria','Parra')

print(f'Estudiante 1 : {Estudiante1.name} {Estudiante1.lastname}')


Estudiante1.hablar()
print(Estudiante1.sumar(10,20))
print(Estudiante1.get_code())
print(Estudiante1.set_code('El codigo ha cambiado'))
print(Estudiante1.get_code())


# No se puede llamar porque es un metodo privado
# Estudiante1.__estudiar()


