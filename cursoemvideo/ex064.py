cont = soma = 0
num = int(input('Digite um número(999 encerra o programa): '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número(999 encerra o programa): '))

print('A quantidade de números informado foi {}.'.format(cont))
print('A soma dos números digitados foi {}.'.format(soma))
