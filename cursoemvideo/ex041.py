from datetime import date

ano = int(input('Qual ano que você nasceu? '))

idade = date.today().year - ano

print('Sua idade é {}. '.format(idade), end='')
if idade < 1:
    print('Não é possivel ser atleta nessa idade!')
elif idade <= 9:
    print('Você será um aleta MIRIM!')
elif idade <= 14:
    print('Você será um aleta INFANTIL')
elif idade <= 19:
    print('Você será um aleta JUNIOR')
elif idade <= 20:
    print('Você será um aleta SÊNIOR')
else:
    print('Você será um aleta MASTER')
