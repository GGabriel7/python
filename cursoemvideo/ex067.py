from time import sleep

num = 0

while True:
    num = int(input('Digite um número para ver a tabuada (NÚMERO NEGATIVO ENCERRA!): '))
    print('-=-' * 5)

    if num < 0:
        break

    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')

    sleep(1.5)
    print('-=-' * 5)

print('ENCERRADO!')

