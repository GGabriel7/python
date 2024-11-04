from time import sleep
from random import randint

num = int(input('QUANTOS JOGOS DA MEGA SENA QUER SORTEAR? '))
print('CARREGANDO...')

for c in range(0, num):
    aleatorio = []
    quant = 0
    sleep(1)

    while True:
        ale = randint(0, 60)
        if ale not in aleatorio:
            aleatorio.append(ale)
            quant += 1
        if quant == 6:
            break

    aleatorio.sort()

    print(f'{c + 1}° Jogo: {aleatorio}')

    del aleatorio
