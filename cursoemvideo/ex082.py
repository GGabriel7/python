impar = []
par = []
num = []

while True:
    numero = int(input('Digite mais um número: '))

    num.append(numero)

    if numero % 2 == 0:
        par.append(numero)

    if numero % 2 == 1:
        impar.append(numero)

    while True:
        esc = input('Quer continuar?[S/N] ').strip().upper()
        if esc == 'S':
            print('-=' * 20)
            break

        if esc == 'N':
            print('=-' * 20)
            break

    if esc == 'N':
        break

print(f'Lista com TODOS os valores: {num}')
print(f'Lista com os valores PAR: {par}')
print(f'Lista com os valores IMPAR: {impar}')
