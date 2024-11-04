valor = [[], []] #Declara 2 listas dentro de uma lista

for c in range(1, 8):
    val = int(input('VALOR: '))
    if val % 2 == 0:
        valor[0].append(val) #coloca os pares dentro da primeira lista da lista VALOR
    else:
        valor[1].append(val) #coloca os pares na segunda lista da lista VALOR

valor[0].sort()
valor[1].sort()

print(f'Valores PARES: {valor[0]}')
print(f'Valores IMPARES: {valor[1]}')
