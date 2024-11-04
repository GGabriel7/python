from datetime import date

ano = int(input('Em que ano você nasceu? '))

idade = date.today().year - ano

if idade < 18:
    faltam = 18 - idade
    print('Sua idade é {}, deverá se alistar em {} anos, em {}.'.format(idade, faltam, date.today().year - faltam))
elif idade == 18:
    print('Sua idade é {}, é hora de se alistar.'.format(idade))
else:
    passou = idade - 18
    print('Sua idade é {}, já passou {} desde que deveria se alistar, deveria ter se alistado em {}.'.format(idade, passou, date.today().year - passou))
