num = []

while True:
    numero = int(input('Digite um número: '))

    num.append(numero)

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

print(f'Voce digitou {len(num)} números.')

num.sort(reverse=True)
print(f'LISTA EM ORDEM DECRESCENTE: {num}')

if 5 in num:
    print('SIM, tem 5')
else:
    print('NÃO tem 5')
