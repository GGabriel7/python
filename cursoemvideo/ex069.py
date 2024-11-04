print('=-=' * 5, 'LENDO DADOS', '=-=' * 5)

pessoas_maior = 0
homens = 0
mulher_20 = 0
parar = []

while True:
    parar = []
    sexo = input('Qual seu sexo? [M/F] ').strip().upper()
    print('=-=' * 7)

    if sexo == 'M':
        homens += 1
        idade = int(input('Digite sua idade: '))
        print('=-=' * 7)
        if idade > 18:
            pessoas_maior += 1

    if sexo == 'F':
        idade = int(input('Digite sua idade: '))
        print('=-=' * 7)
        if idade < 20:
            mulher_20 += 1
        if idade >= 18:
            pessoas_maior += 1

    if sexo == 'F' or sexo == 'M':
        while 'N' != parar != 'S':
            parar = input('Quer continuar? [S/N] ').strip().upper()
            print('=-=' * 7)

    if parar == 'S':
        print('=-=' * 7)

    if parar == 'N':
        break

print(f'{pessoas_maior} pessoa(s) cadastrada(s) tem mais de 18 anos.')
print(f'{homens} homen(s) foram cadastrado(s). ')
print(f'{mulher_20} mulher(es) cadastrada(s) tem menos de 20 anos.')
