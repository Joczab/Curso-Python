from Cuenta.Cuenta import Cuenta
from Cuenta.Validaciones_de_cuenta import random_acount_number, saldo_inicial,valid_account
from Usuario.Validaciones_usuario import crear_usuario, ingresar_usuario, validar_cedula
from Usuario.Usuario import Usuario
from Validaciones import mostrar_menu, validar_opcion


class SistemaBancario:
    '''Clase de sistema bancario'''
    def __init__(self,usuarios : list[Usuario], sesion: Usuario = None):
        self.usuarios = usuarios
        self.sesion = sesion
    
    def main(self):
        '''Funciones principales'''
        opciones = [
            {"accion": "Crea tu usuario", "valor": "1"},
            {"accion": "Iniciar sesión", "valor": "2"},
            {"accion": "Finalizar", "valor": "3"},
        ]
        
        is_not_exit = True
        
        while is_not_exit:
            print('Elija una opcion:\n')
            mostrar_menu(opciones)
            
            opcion_selec = validar_opcion(opciones)
            
            if opcion_selec == 1:
                nuevo_usuario = crear_usuario()
                
                usuario_existe = [usuario for usuario in self.usuarios if nuevo_usuario.username == usuario.username or nuevo_usuario.cedula == usuario.cedula]
            
                if len(usuario_existe)>0:
                    print('El usuario ya existe\n')
                else:
                    self.usuarios.append(nuevo_usuario)
            
            elif opcion_selec == 2:
                self.iniciar_sesion()
                
                if self.sesion is not None:
                    self.menu_usuario()
                    
    def iniciar_sesion(self):
        '''Funcion de iniciar sesion'''
        user = ingresar_usuario(self.usuarios)
        
        if len(user) == 0:
            print('Crendenciales invalidadas.\n')
        else:
            self.sesion = user[0]
    
    def menu_usuario(self):
        opciones = [
            {"accion": "Crear cuenta bancaria", "valor": "1"},
            {"accion": "Depositar", "valor": "2"},
            {"accion": "Retirar", "valor": "3"},
            {"accion": "Transferir", "valor": "4"},
            {"accion": "Cerrar sesión", "valor": "5"}
        ]

        is_not_back = True
        
        while is_not_back:
            print("Elija una opcion:\n")
            mostrar_menu(opciones)
            
            opcion_selec = validar_opcion(opciones)
            
            if opcion_selec == 1:
                self.crear_cuenta()
            elif opcion_selec == 2:
                self.depositar()
            elif opcion_selec == 3:
                self.retirar()
            elif opcion_selec == 4:
                self.transferir()
            elif opcion_selec == 5:
                is_not_back = self.cerrar_sesion()
                
    def crear_cuenta(self):
        '''Funcion de crear cuenta'''
        usuario = self.sesion
        
        if usuario.cuentas is not None:
            print('Usted ya posee una cuenta bancaria\n')
        else:
            numero_de_cuenta = random_acount_number()
            
            saldo = saldo_inicial('Saldo inicial de la cuenta:\n')
            
            usuario.cuentas = [Cuenta(numero_de_cuenta,saldo)]
            
            print(f'Su nuevo numero de cuenta es: {numero_de_cuenta}\n')
            print(f'Su saldo de la cuenta es:{saldo}$\n')
    
    def depositar(self):
        '''Funcion de depositar'''
        usuario = self.sesion
        
        if usuario.cuentas is None:
            print('Usted no posee una cuenta bancaria.\n')
        else:
            saldo = saldo_inicial('Saldo a depositar:\n')
            
            usuario.cuentas[0].depositar(saldo)
            print('Deposito realizado con exito.\n')
            print(f'Su saldo actualizado es: {usuario.cuentas[0].saldo}$')
    
    def retirar(self):
        '''Funcion de retirar'''
        usuario = self.sesion
        
        if usuario is None:
            print('No posee una cuenta bancaria.\n')
        else:
            print(f'Saldo actual:{usuario.cuentas[0].saldo}$')

            saldo = saldo_inicial('Saldo a retirar:\n')
            
            if saldo > usuario.cuentas[0].saldo:
                print('Fondos insuficientes.')
            else:
                usuario.cuentas[0].retirar(saldo)
                print('Retiro realizado')
                print(f'Su saldo restante es:{usuario.cuentas[0].saldo}$')
                
    def transferir(self):
        '''Funcion de transferir'''
        
        usuario = self.sesion
        
        if usuario.cuentas is None:
            print('Usted no posee una cuenta')
        else:
            cedula = validar_cedula('Cedula de la persona a transferir:\n')
            
            while (len([usuario for usuario in self.usuarios if usuario.cedula == cedula])==0):
                
                print('La cedula proporcionada no pertenece a ningun usuario, intente con otra cedula.\n')
                cedula = validar_cedula('Cedula de la persona a transferir:\n')
            
            usuario_a_transferir = [usuario for usuario in self.usuario if usuario.cedula == cedula]
            
            print(f'Datos del usuario con cedula:{cedula}')
            print(f'Numero de cuenta: {usuario_a_transferir[0].cuentas[0].account_id}')
            
            numero_de_cuenta = valid_account()
            
            if numero_de_cuenta != usuario_a_transferir[0].cuentas[0].account_id:
                print('Numero de cuenta incorrecto.\n')
            else:
                print(f'Saldo actual: {usuario.cuentas[0].saldo}$')
                
                saldo = saldo_inicial('Saldo a transferir.\n')
                
                if saldo_inicial > usuario.cuentas[0].saldo:
                    print('Fondos insuficientes.\n')
                else:
                    usuario_a_transferir[0].cuentas[0].depositar(saldo)
                    usuario.cuentas[0].retirar(saldo)
                    print('Transferencia realizada con exito.')
                    print(f'Saldo Transferido: {saldo}')
                    print(f'Su saldo restante:{usuario.cuentas[0].saldo}$')
        
    def cerrar_sesion(self):
        '''Funcion de cerrar sesion'''
        self.sesion = None
        return False