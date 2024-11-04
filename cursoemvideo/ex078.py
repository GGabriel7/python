num = []
maior = menor = 0

for c in range(0, 5):
    num.append(int(input(f'DIGITE UM VALOR. {c}°: ')))

print(f'LISTA: {num}')

print(f'O MAIOR NÚMERO É {max(num)}. NA POSIÇÃO: ', end='')
for mai in enumerate(num):
    if mai[1] == max(num):
        maior = mai[0]
        print(f'{maior}...', end ='')

print(f'\nO MENOR NÚMERO É {min(num)}. NA POSIÇÃO ', end='')
for men in enumerate(num):
    if men[1] == min(num):
        menor = men[0]
        print(f'{menor}...', end='')
print()
