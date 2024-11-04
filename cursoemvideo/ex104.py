def LeiaInt(a):
    while True:
        print(a, end='')
        global num
        num = input()
        if not num.isdigit():
            print('\033[0;31mErro! Digite um número inteiro!\033[m')
        else:
            return int(num)

num = LeiaInt('Digite um número: ')
print(f'Você digitou o número {num}.')
