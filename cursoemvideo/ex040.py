n1 = float(input('Qual sua nota? '))
n2 = float(input('Qual sua outra nota? '))

media = (n1 + n2) / 2

if n1 or n2 < 0:
    print('ERRO!')

elif n1 or n2 > 10:
    print('ERRO!')

else:
    print('Sua média é {}'.format(media))
    if media < 5:
        print('REPROVADO!')
    elif 5 < media < 6.9:
        print('RECUPERAÇÃO!')
    else:
        print('APROVADO!')
