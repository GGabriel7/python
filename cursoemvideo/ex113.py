def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(f'\033[31mEntrada invalida. Número não é INTEIRO.\033[m')
        except KeyboardInterrupt:
            print('\nEncerrado')
            return 0


def LeiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print('\033[31mEntrada invalida. Número não é REAL.\033[m')
        except KeyboardInterrupt:
            print('\nEncerrado')
            return 0



numi = LeiaInt('Digite um número INTEIRO: ')
numf = LeiaFloat(('Digite um número REAL: '))

print(f'Voce digitou o numero REAL {numf}')
print(f'Voce digitou o numero INTEIRO {numi}')

