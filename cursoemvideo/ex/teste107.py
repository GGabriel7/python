from ex107 import moeda

num = float(input('Digite um valor: R$'))

print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando 10% de {num} é {moeda.aumentar(num, 10)}')
print(f'Removendo 10% de {num} é {moeda.diminuir(num, 10)}')