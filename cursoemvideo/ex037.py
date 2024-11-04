n = int(input('Escolha um número decimal inteiro para converter: '))

binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)

e = int(input('''Ecolha um dos valores abaixo para converter:
[1] Binário
[2] Octal
[3] Hexadecimal\n'''))

if e == 1:
    print('A conversão de {} para binário é {}'.format(n, binario[2:]))
elif e == 2:
    print('A conversão de {} para octal é {}'.format(n, octal[2:]))
elif e == 3:
    print('A conversão de {} para hexadecimal é {}'.format(n, hexadecimal[2:]))
else:
    print('Opção invalida!')
