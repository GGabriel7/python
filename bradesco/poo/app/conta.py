class Conta:
    def __init__(self, titular, numero, saldo):   

        self._titular = titular
        self._numero = numero
        self._saldo = 0

        @property
        def saldo(self):
            return self._saldo
        
        @saldo.setter
        def saldo(self, saldo):
            if (saldo<0):
                print("O saldo não pode ser negativo")
            else:
                self._saldo = saldo

    def saque(self, valor):
        if(self._saldo >= valor):
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")

    def deposito(self, valor):
        self._saldo+=valor
        
    def extrato(self):
         print(f"Cliente: {self._titular} | Saldo atual {self._saldo}")