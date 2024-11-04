resp = 0
media = 0
divide = 0
valores = []

while resp != 2:
    resp = int(input('Você quer digitar um número?\n[1] SIM\n[2] NÃO\n'))
    if resp == 1:
        num = float(input('Digite um valor: '))
        media += num
        divide += 1
        valores.append(num)

print('A média dos números informados é: {}'.format(media / divide))
print('O maior valor informado foi: {}'.format(max(valores)))
print('O menor valor informado foi: {}'.format(min(valores)))
