class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.a = ladoA
        self.b = ladoB


    def mudaValor(self, novoA, novoB):
        self.a = novoA
        self.b = novoB

    
    def retornaLado(self):
        print(f'O Retângulo possui dimensões {self.a}m x {self.b}m')


    def area(self):
        return self.a * self.b