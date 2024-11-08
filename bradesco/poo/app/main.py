class Main:
    pass

print('Testando o projeto')

from cliente import Cliente
from conta import Conta

c1 = Cliente("Gabriel", "85 99429-8811")
conta = Conta(c1.get_nome(), 6565, 0)

conta.deposito(100)
conta.saque(50)
conta.extrato()