num1 = int(input('digite um numero:'))
num2 = int(input('digite um numero:'))
num3 = int(input('digite um numero:'))

lit = (num1, num2, num3)

ordlit = sorted(lit)

print('o menor numero é {}'.format(ordlit[0]))

print('o maior numero é {}'.format(ordlit[2]))