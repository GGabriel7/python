from random import randint

def sortea(list):
    print(f'Os números sorteador foram: ', end='')
    for c in range(0, 5):
        ale = randint(0, 9)
        list.append(ale)
        print(f'{ale} ', end = '')
    print()

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos números paras é {soma}.')

numeros = []
sortea(numeros)
somaPar(numeros)
