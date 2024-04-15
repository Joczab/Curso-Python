class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.sesion = None

    def menu_inicio_sesion(self):
        nombre_usuario = input('Nombre de usuario:\n')
        contraseña = input('Contraseña:\n')
        usuario = next((usuario for usuario in self.usuarios if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña), None)
        
        if usuario:
            self.sesion = usuario
            self.menu_usuario()
        else:
            print('Nombre de usuario o contrasena incorrecto.')
            
    def menu_usuario(self):
        ejecutar=True
        
        while ejecutar:
            print('Menu de usuario.\n')
            print('1. Crear cuenta bancaria.')
            print('2. Depositar.')
            print('3. Retirar.')
            print('4. Transferir.')
            print('5. Cerrar sesion.')
            option = input('Seleccione una opcion:\n')
            match(option):
                case '1':
                    pass
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    ejecutar=False