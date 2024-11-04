frase = input('Digite uma frase: ').strip().upper()

espaco = frase.replace(' ', '')

invertida = espaco[::-1]

print('{} invertido é {}'.format(frase, invertida))

if espaco == invertida:
    print('SIM, é um palíndromo')
else:
    print('NÃO, não é um palíndromo')
