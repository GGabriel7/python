from datetime import date

maior = []
menor = []

for c in range(0, 7):
    ano = int(input('Ano da pessoa {}: '.format(c)))

    idade = date.today().year - ano
    if idade >= 18:
        maior.append('Pessoa {} é maior de idade'.format(c))
    else:
        menor.append('Pessoa {} é menor de idade'.format(c))

print('n')

for pessoa in maior:
    print(pessoa)

print('\n')

for pessoa in menor:
    print(pessoa)
