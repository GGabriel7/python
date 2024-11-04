lista = ('Mercusys', 250,
         'Huawei', 300,
         'TP-Link', 180,
         'ONU', 50,
         'ONT', 350,
         'D-Link', 125,
         'Intelbras', 150,
         'SW', 300,
         'RouterBoar', 350,
         'Multilaser PRO', 150,
         'Conectores (100u)', 20,
         'Cabo (M)', 3.5)

print('-=' * 22)
print(f'{"LISTA":^44}')
print('-=' * 22)

for posicao in range(0, len(lista), 2):
    print(f'{lista[posicao]:.<34} ', end='')
    print(f'R$ {lista[posicao + 1]:>7.2f}')
print('-='*22)

for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<34} ', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-='*22)
