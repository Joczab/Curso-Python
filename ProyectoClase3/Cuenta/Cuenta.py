class Cuenta:
    def __init__(self,num_cuenta,saldo):
        
        self.num_cuenta = num_cuenta
        self.saldo = saldo
        
    def depositar(self,saldo_agregado):  
        self.saldo = self.saldo + saldo_agregado
        
    def retirar(self,saldo_retirado):
        self.saldo = self.saldo - saldo_retirado
    
    
