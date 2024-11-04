from time import sleep

def contador(a, b, c):
    print(f'Contador começando de {a} indo até {b} pulando de {c} em {c}')
    print('--' *20)

    if c < 0:
        c *= -1
    if c == 0:
        c = 1

    if a < b:
        cont = a
        while cont <= b:
            print(cont, end=' -> ', flush=True)
            cont += c
            sleep(0.1)
    else:
        cont = a
        while cont >= b:
            print(cont, end=' -> ', flush=True)
            cont -= c
            sleep(0.1)

    print('FIM!')
    print('--' *20)

contador(1, 10, 1)
contador(10, 1, 2)

a = int(input('Começa em qual número: '))
b = int(input('Termina em qual núemro: '))
c = int(input('Pula de quanto em quanto: '))

contador(a, b, c)
