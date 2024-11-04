nome = ('ZERO', 'UM', 'DOIS', 'TRES',
        'QUATRO', 'CINCO', 'SEIS', 'SETE',
        'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE',
        'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS',
        'DIZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

esc = ''

while True:
    num = int(input('Digite um número entre 1 e 20: '))
    if num < 0 or num > 20:
        while num < 0 or num > 20:
            num = int(input('VALOR INCORRERO! Entre 1 e 20: '))

    print(f'Você digitou {nome[num]}.')
    print('-=-' * 20)

    while True:
        esc = input('Quer continuar? [S/N] ').strip().upper()

        if esc == 'S':
            print('-=-' * 20)
            break

        if esc == 'N':
            break

    if esc == 'N':
        break

print('FIM!')
