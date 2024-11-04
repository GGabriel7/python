n = float(input('Quanto dinheiro você tem na carteira? \n R$'))

d = n / 4.92

if n < 4.92:
    print('Não pode comprar nenhum dolar')
else:
    print('Você pode comprar {:.2f} dolares.'.format(d))
    print(f'Você pode comprar {d} dolares.')