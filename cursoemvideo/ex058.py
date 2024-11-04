from random import randint

print('Estou pensando em número entre 1 e 100. Duvido você adivinhar em 7 tenttivas.')

sorte = randint(1, 100)
num = int(input('1° tentativa: '))
quant = 1

while sorte != num and quant != 7:
    quant += 1
    if num > sorte:
        print('ERROU! MENOS... {}'.format(quant), end='')
        num = int(input('° Tentativa: '))
    else:
        print('ERROU! MAIS... {}'.format(quant), end='')
        num = int(input('° Tentativa: '))

if num == sorte:
    print('ACERTOU!!! O número que eu estava pensando era {}. Você precisou de {} tentativas.'.format(sorte, quant))
else:
    print('Você ultrapassou o número de tentativas. O número era {}'.format(sorte))
