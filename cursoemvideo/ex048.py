print('Esses são todos os número MULTIPLOS DE 3 entre 1 e 500: ')

for c in range(3, 500, 3):
    print(c, end='')
    print(' ', end='')
print('\n')

print('E essa é a soma entre todos os MULTIPLOS DE 3 entre 1 e 500: ', end='')

soma = 0

for i in range(0, 500, 3):
    soma += i #Ou soma = c + soma
print('{}'.format(soma))
