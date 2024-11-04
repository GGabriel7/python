km = float(input('Qual a distancia da sua viagem em km? '))

if km <= 0:
    print('Isso não é uma viagem.')
elif km <= 200:
    print('O valor da sua viagem será R${}'.format(km * 0.5))
else:
    print('O valor da sua viagem será R${}'.format(km * 0.45))