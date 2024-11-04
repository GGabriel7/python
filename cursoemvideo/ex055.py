pesos = []

for c in range(1, 6):
    peso = int(input('Peso da pessoa {}: Kg'.format(c)))
    pesos.append(peso)

print('n')

maior = max(pesos)
menor = min(pesos)

print('Maior peso {}'.format(maior))
print('Menor peso {}'.format(menor))
