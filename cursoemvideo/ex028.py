from random import randint
from time import sleep

numero = int(input('Eu estou pensando em um número entre 1 e 5, qual você acha que é esse número? '))

print('PROCESSANDO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
sleep(1)

aleatorio = randint(1, 5)

if 0 < numero < 6:
    if aleatorio == numero:
        print('Você escolheu {} e era exatamente o número {} que eu pensei'.format(numero, aleatorio))
    elif aleatorio != numero:
        print('Você escolheu {} mas eu estava pensando no número {}'.format(numero, aleatorio))
else:
    print('Ué. Esse número está fora da escala que eu estava pensando.')