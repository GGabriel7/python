sal = float(input('Digite o valor do seu salario: R$'))

if sal <= 2000:
    print('O seu salário de R${} ficará R${:.2f}.'.format(sal, sal * 1.15))
else:
    print('O seu salário de R${} ficará R${:.2f}.'.format(sal, sal * 1.10))