p = float(input('Qual o preço do produto? \n'))

d = p - (p*5/100)

print('O valor do produto com 5% é de R${:.2f}'.format(d))
print(f'O valor do produto com 5% é de R${d}')