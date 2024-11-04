num = []

while True:
    numero = int(input('Digite um número: '))
    
    if numero not in num:
        num.append(numero)
        print('NUMÉRO ADICONADO COM SUCESSO')

    else:
        print('NÚMERO JÁ HAVIA SIDO ADICIONADO')

    while True:
        esc = input('Quer continuar?[S/N] ').strip().upper()
        if esc == 'S':
            break
        if esc == 'N':
            print('SAINDO...')
            break

    if esc == 'N':
        break

num.sort()

print(f'LISTA EM ORDEM CRESCENTE: {num}')

num.sort(reverse=True)

print(f'LISTA EM ORDEM CRESCENTE: {num}')
