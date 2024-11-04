from ex110 import moeda

num = float(input('Digite um valor: R$'))

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10% de {moeda.moeda(num)} é {(moeda.aumentar(num, 10, True))}')
print(f'Removendo 10% de {moeda.moeda(num)} é {moeda.diminuir(num, 10)}')

print('--' * 10)

moeda.resumo(num, 85, 30)