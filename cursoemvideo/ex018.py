from math import sin, cos, tan, radians

a = float(input('Esolha um ângulo: '))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O seno é {:.2f} \nO coseno é {:.2f} \nE a tangente é {:.2f}'.format(s, c, t))
print(f'O seno é {s} \nO coseno é {c} \nA tangente é {t}')
