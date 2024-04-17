from Usuario.Usuario import Usuario
from Validaciones import no_vacio, entero_valido

def validar_nombre():
    ''' Funcion para validar nombre'''
    nombre = no_vacio('Nombre:\n')
    
    while nombre.isdigit():
        print('El nombre no puede tener numeros.\n')
        nombre = no_vacio('Nombre:\n')
    return nombre

def validar_cedula(text):
    '''funcion para validar cedula'''
    cedula = entero_valido(text,'La cedula solo debe contener numeros.\n')
    return cedula

def validar_apellido():
    ''' Funcion para validar apellido'''
    
    apellido = no_vacio('Apellido:\n')
    
    while apellido.isdigit():
        print('El apellido no puede tener numeros.\n')
        apellido = no_vacio('Apellido:\n')
    return apellido

def validar_username():
    '''funcion para validar username'''
    
    username = no_vacio('Nombre de usuario\n')
    
    while username.isdigit():
        print('El nombre de usuario no puede tener solo numeros\n')
        username = no_vacio('Nombre de usuario\n')
    return username

def validar_contraseña():
    '''Funcion para validar contraseña'''
    contraseña = no_vacio('Contraseña:\n')
    
    return contraseña

def crear_usuario():
    ''' Funcion de crear usuario'''
    
    nombre = validar_nombre()
    apellido = validar_apellido()
    cedula = validar_cedula('Cedula:\n')
    username = validar_username()
    contraseña = validar_contraseña()
    
    return Usuario(nombre,apellido,cedula,username,contraseña)

def ingresar_usuario(usuarios: list[Usuario]):
    '''Funcion de ingresar usuario'''
    
    username = validar_username()
    contraseña = validar_contraseña()
    
    validar_usuario = [usuario for usuario in usuarios if username == usuario.username and usuario.validar_contraseña(contraseña) is True]
    
    return validar_usuario