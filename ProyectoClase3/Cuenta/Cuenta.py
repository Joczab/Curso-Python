class Cuenta:
    def __init__(self,account_id,saldo):
        
        self.account_id = account_id
        self.saldo = saldo
        
    def depositar(self,saldo_agregado):  
        self.saldo = self.saldo + saldo_agregado
        
    def retirar(self,saldo_retirado):
        self.saldo = self.saldo - saldo_retirado
    
    
