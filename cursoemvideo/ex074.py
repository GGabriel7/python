from random import randint

alea = []

print('Esses são os valores sorteador: ', end = '')

for ale in range(1, 6):
    ale = randint(0, 9)
    print(f'{ale} ', end = '')
    alea.append(ale)

print(f'\nEsse foi o maior: {max(alea)}')
print(f'Esse foi o menor: {min(alea)}')
