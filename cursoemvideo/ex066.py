num = 0
soma = 0

while True:
    num = int(input('Digite um número (999 para o programa): '))

    if num == 999:
        break

    soma += num

print(f'A soma dos números informado é {soma}')
