from funcionario import Funcionario

funcionario = Funcionario('Gabriel', 'jgabrielnr31@gmail.com')

funcionario.cadastroHora('Jan', 220)
funcionario.cadastroHora('Fev', 220)
funcionario.cadastroSalarioHora('Jan', 7)
funcionario.cadastroSalarioHora('Fev', 7)

print(funcionario)
print(funcionario.calculaSalario('Jan'))
print(funcionario.calculaSalario('Fev'))
