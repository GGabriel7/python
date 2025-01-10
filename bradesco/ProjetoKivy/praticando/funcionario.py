class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salarioHora = {}


    def cadastroHora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    
    def cadastroSalarioHora(self, mes, valor):
        if (mes not in self.salarioHora):
            self.salarioHora[mes] = valor

    
    def calculaSalario(self, mes):
        if (mes not in self.horas) or (mes not in self.salarioHora):
            print('Mês Inexistente!')
        else:
            return self.horas[mes] * self.salarioHora[mes]
        
    
    def __repr__(self):
        return f'Funcionário: {self.nome}, \nEmail: {self.email}, \nhoras/mes: {self.horas}, \nsalário/hora: {self.salarioHora}'