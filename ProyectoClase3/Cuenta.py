class Cuentas:
    def __init__(self,num_cuenta,saldo):
        
        self.num_cuenta = num_cuenta
        self.saldo = saldo
        
    def depositar_saldo(self,saldo_agregado):  
        self.saldo = self.saldo + saldo_agregado
        return self.saldo
    
    def retirar_saldo(self,saldo_retirado):
        if self.saldo >= saldo_retirado:
            self.saldo = self.saldo - saldo_retirado
            return self.saldo
        else:
            print('Fondos insuficientes.\n')
            return None
    
""" # crear una cuenta con el saldo de 1000
cuenta = Cuentas(12345, 1000)
print(f'Datos de la cuenta: {cuenta.num_cuenta} {cuenta.saldo}')
# Depositar 500
deposito = 500
cuenta.depositar_saldo(deposito)
print(f'Depositaste: {deposito}, ahora tu saldo es {cuenta.saldo}')
# Retirar 200
retiro1 = 200
cuenta.retirar_saldo(retiro1)
print(f'Retiraste {retiro1}, ahora tu saldo es {cuenta.saldo}')
# Retirar 900
retiro2 = 2000
cuenta.retirar_saldo(retiro2)
print(f'Retiraste {retiro2}, ahora tu saldo es {cuenta.saldo}')
 """    