d = int(input('Quantos dias você passou com o carro? '))
k = float(input('E quantos Km andou? '))

vd = d * 60
vk = k * 0.15
vt = vd + vk

print('O valor a pagar será R${}'.format(vt))
print(f'O valor a pafar será R${vt}')
