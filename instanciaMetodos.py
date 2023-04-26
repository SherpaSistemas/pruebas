class Movimientos:
    def __init__(self, nombre):
        self.saldo=0
        self.propietario=nombre
    
    def deposito(self,cantidad):
        self.saldo=self.saldo+cantidad
        return self.saldo

    def retiro(self,cantidad):
        if cantidad>self.saldo:
            return ('Fondos insuficientes')
        self.saldo=self.saldo-cantidad
        return (self.saldo)
        
L=Movimientos('Uriel')
L.deposito(1000)
print(L.saldo)

cctm=Movimientos('CCTMéxico')
cctm.deposito(100)
cctm.retiro(90)
print('El saldo disponible de CCTM es: ', cctm.saldo)
        
