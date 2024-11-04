nove = 0
par = 0

num = (int(input(': ')), int(input(': ')), int(input(': ')), int(input(': ')))

for nov in range(0, 4):
    if num[nov] == 9:
        nove += 1

for pa in range(0, 4):
    if num[pa] % 2 == 0:
        par += 1

print(f'NUMEROS: {num}')
print(f'NOVE(S): {nove}')
print(f'PAR(ES): {par}')

if 3 in num:
    for tre in range(0, 4):
        if num[tre] == 3:
            print(f'O TRÊS NA {tre + 1}° POSIÇÃO')
            break
else:
    print('Não tem 3')
