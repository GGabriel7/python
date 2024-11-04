n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha outro numero: '))
n3 = int(input('Escolha mais um numero: '))

if n1 > n2 > n3:
    print('O maior é o {} e o menor é {}.'.format(n1, n3))
if n1 > n3 > n2:
    print('O maior é o {} e o menor é {}.'.format(n1, n2))
if n2 > n1 > n3:
    print('O maior é o {} e o menor é {}'.format(n2, n3))
if n2 > n3 > n1:
    print('O maior é o {} e o menor é {}'.format(n2, n1))
if n3 > n2 > n1:
    print('O maior é o {} e o menor é {}'.format(n3, n1))
if n3 > n1 > n2:
    print('O maior é o {} e o menor é {}'.format(n3, n2))