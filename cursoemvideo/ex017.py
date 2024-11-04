from math import sqrt

a = float(input('Cateto: '))
b = float(input('Cateto: '))

h = sqrt(a**2 + b**2)

print('{:.2f}'.format(h))
