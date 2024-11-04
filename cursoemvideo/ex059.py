from time import sleep

n1 = float(input('DIGITE UM NÚMERO: '))
n2 = float(input('DIGITE OUTRO NÚMERO: '))

esc = 0

while esc != 5:
    esc = int(input('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR\nEscolha: '))

    if esc == 1:
        print('-=-' * 10)
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        print('-=-' * 10)

    elif esc == 2:
        print('-=-' * 10)
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        print('-=-' * 10)

    elif esc == 3:
        if n1 > n2:
            print('-=-' * 10)
            print('O maior número foi o primerio digitado, o {}'.format(n1))
            print('-=-' * 10)
        elif n2 > n1:
            print('-=-' * 10)
            print('O maior número foi o segundo digitado, o {}'.format(n2))
            print('-=-' * 10)
        else:
            print('-=-' * 10)
            print('São iguais.')
            print('-=-' * 10)

    elif esc == 4:
        print('-=-' * 10)
        n1 = float(input('DIGITE UM NÚMERO: '))
        n2 = float(input('DIGITE OUTRO NÚMERO: '))
        print('-=-' * 10)

    elif esc == 5:
        print('FINALIZANDO...')

    else:
        print('-=-' * 10)
        print('VALOR INCORRETO.')
        print('-=-' * 10)

    sleep(1.5)

    # O número 5 irá sair do programa.

print('OBRIGADO POR PARTICIPAR!!!')
