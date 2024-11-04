valor = []

for a in range(0, 3):
    val1 = int(input(f'VALOR: (0, {a}) '))
    valor.append(val1)
for a in range(0, 3):
    val1 = int(input(f'VALOR: (1, {a}) '))
    valor.append(val1)
for a in range(0, 3):
    val1 = int(input(f'VALOR: (2, {a}) '))
    valor.append(val1)

for a in valor[:3]:
    print(f'[{a:^5}] ', end = '')
del valor[:3]

print()

for a in valor[:3]:
    print(f'[{a:^5}] ', end = '')
del valor[:3]

print()

for a in valor:
    print(f'[{a:^5}] ', end = '')

print()

#Outra resolução:
for s in range(0, 3):
    print('=-' * 10)

valor = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for colun in range(0, 3):
        valor[linha][colun] = int(input(f'DIGITE: [{linha}, {colun}]'))

for linha in range(0, 3):
    for colun in range(0, 3):
        print(f'[{valor[linha][colun]:^5}]', end = '')
    print()
