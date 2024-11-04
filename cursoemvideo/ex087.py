valor = []
soma = soma2 = maior = 0

for a in range(0, 3):
    val1 = int(input(f'VALOR: (0, {a}) '))
    valor.append(val1)
    if val1 % 2 == 0:
        soma += val1
soma2 += val1

for a in range(0, 3):
    val1 = int(input(f'VALOR: (1, {a}) '))
    valor.append(val1)
    if val1 % 2 == 0:
        soma += val1
    if val1 > maior:
        maior = val1
soma2 += val1

for a in range(0, 3):
    val1 = int(input(f'VALOR: (2, {a}) '))
    valor.append(val1)
    if val1 % 2 == 0:
        soma += val1
soma2 += val1

print('=-' *20)

for a in valor[:3]:
    print(f'[  {a}  ] ', end = '')
del valor[:3]

print()

for a in valor[:3]:
    print(f'[  {a}  ] ', end = '')
del valor[:3]

print()

for a in valor:
    print(f'[  {a}  ] ', end = '')

for i in range(0, 3):
    print('=-' *20)

print(f'SOMA dos valores PARES: {soma}')
print(f'SOMA dos valores da TERCEIRA COLUNA: {soma2}')
print(f'O MAIOR VALOR da SEGUNDA LINHA: {maior}')

#Outra resolução:
for s in range(0, 3):
    print('=-' * 10)

valor = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
outrasoma = outrasoma2 = outromaior = 0

for linha in range(0, 3):
    for colun in range(0, 3):
        valor[linha][colun] = int(input(f'DIGITE: [{linha}, {colun}]'))
        if valor[linha][colun] % 2 == 0:
            outrasoma += valor[linha][colun]

for linha in range(0, 3):
    outrasoma2 += valor[linha][2]

for colun in range(0, 3):
    if valor[1][linha] > outromaior:
        outromaior = valor[1][linha]

for linha in range(0, 3):
    for colun in range(0, 3):
        print(f'[{valor[linha][colun]:^5}]', end = '')
    print()

print(f'SOMA dos valores PARES: {outrasoma}')
print(f'SOMA dos valores da TERCEIRA COLUNA: {outrasoma2}')
print(f'O MAIOR VALOR da SEGUNDA LINHA: {outromaior}')
