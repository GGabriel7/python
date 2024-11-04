from random import randint

esc = 0
cont = 0

while True:
    print('=-=' * 7)
    esc = int(input('[1] IMPAR\n[2] PAR\nESCOLHA: '))

    comp = randint(0, 10)

    if esc == 1:

        print('=-=' * 7)
        num = int(input('Escolha um número: '))

        if (num + comp) % 2 == 1:
            print('=-=' * 7)
            print(f'GANHOU! Você escolheu {num} e eu ecolhi {comp}. Sendo assim, {num + comp} é IMPAR')
            cont += 1
        else:
            print('=-=' * 7)
            break

    if esc == 2:

        print('=-=' * 7)
        num = int(input('Escolha um número: '))

        if (num + comp) % 2 == 0:
            print('=-=' * 7)
            print(f'GANHOU! Você escolheu {num} e eu ecolhi {comp}. Sendo assim, {num + comp} é PAR')
            cont += 1

        else:
            print('=-=' * 7)
            break

if esc == 1:
    print(f'PERDEU. Você escolheu {num} e eu escolhi {comp}. {num + comp} é PAR. eve um seuquencia de {cont} vitoria(s)')

if esc == 2:
    print(f'PERDEU. Você escolheu {num} e eu escolhi {comp}. {num + comp} é IMPAR. Você teve um seuquencia de {cont} vitorias(s)')
