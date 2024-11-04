print('Vamos fazer uma progressão aritmética mostrando os 10 primeiros termos.(PA)')

num = int(input('Escolha um número para começar essa PA: '))
razao = int(input('Qual vai ser a razão dessa PA? '))

print('Essa é a prograssão arítimética de {} pulando de {} em {}: '.format(num, razao, razao))

for c in range(num - 1, num + 9 * razao, razao):
    print(c + 1, end=' -> ')
print('ACABOU')
