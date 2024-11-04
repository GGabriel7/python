n = input('Digite um numero de 0 a 9999: ')

print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

o = int(input('Novamente de 0 a 9999: '))

if 0 < o < 9999:
    print('Unidade: {}'.format(o // 1 % 10))
    print('Dezena: {}'.format(o // 10 % 10))
    print('Centena: {}'.format(o // 100 % 10))
    print('Milhar: {}'.format(o // 1000 % 10))
else:
    print('número incorreto')