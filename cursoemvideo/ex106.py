def helpa(a):
    help(a)

inf = ''
while True:
    inf = str(input('Escolha um comando para verificar: ')).strip().lower()
    if inf == 'sair':
        break
    else:
        helpa(inf)
