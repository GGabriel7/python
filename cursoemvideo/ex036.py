casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('em quantos anos vai pagar? '))

mensal = casa / (anos * 12)
minimo = salario * 0.3 #30% do salario

if mensal > salario * minimo:
    print('Emprestimo NEGADO! A prestação será de {:.2f} e seu salário de R${:.2f} não conseguirá pagar a casa do valor R${:.2f}'.format(mensal, salario, casa))
else:
    print('Emprestimo APROVADO! A prestação será de {:.2f} e seu salário de R${:.2f} CONSEGUIRÁ pagar a casa do valor R${:.2f}'.format(mensal, salario, casa))

