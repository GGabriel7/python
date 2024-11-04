km = float(input('A qual velocidade você estava em km/h? '))

multa = (km - 80)*7

if km < 0:
    print('ERRO! Velocidade NULA')
elif km <= 80:
    print('Você estava no limite permitido')
else:
    print('MULTADO! Seu valor a pagar será de R${:.2f}'.format(multa))