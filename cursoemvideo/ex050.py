soma = 0

for c in range(0, 6):
    num = int(input('Escolha um número para somar: '))
    if num % 2 == 0:
        soma += num
        cont = cont + 1
print('A soma dos números pares é {}.'.format(soma))
