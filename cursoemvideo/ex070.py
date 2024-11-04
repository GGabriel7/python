produtomenor = None
menorvalor = float('inf')
valor_total = maisdemil = 0

print('-=-' * 7, 'LOGINHA', '-=-' *7)

while True:
    parar = []
    produto = input('Nome do produto: ').strip().upper()
    preco = float(input('Valor do produto: R$'))

    valor_total += preco

    if preco > 1000:
        maisdemil += 1

    if preco < menorvalor:
        menorvalor = preco
        produtomenor = produto

    parar = ''
    while 'S' != parar != 'N':
        ('-=-' * 7)
        parar = input('CONTINUAR? [S/N] ').strip().upper()

    if parar == 'S':
        print('-=-' * 7)

    if parar == 'N':
        break

print(f'O valor total das compras foi de R${valor_total}.')
print(f'O produto mais barato foi o {produtomenor}, com valor de R${menorvalor}.')
print(f'{maisdemil} produto(s) custaram mais de R$1000.00.')
