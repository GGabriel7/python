num = int(input('Digite um número para ver seu fatorial: '))

if num < 0:
    print('Não é possivel fatoriar número negaivos')

else:
    fatorial = 1
    contador = 1

    while contador <= num:
        fatorial *= contador
        contador += 1
        print(contador)

    print('O fatorial de {} é {}.'.format(num, fatorial))
