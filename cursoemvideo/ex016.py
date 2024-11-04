from math import floor, trunc

n = float(input('Digite um número: '))
i = floor(n) # deixa o menor número caso sejar colocado casas após a virgula
i2 = trunc(n) # deixa somente o número inteiro

print('O seu valor inteiro é {}'.format(i))
print('O seu valor inteiro é {}'.format(i2))
print('O seu valor inteiro é {}'.format(int(n)))
