n = str(input('Digite seu nome completo: ')).lower().strip()

nome = n.split()

print('Seu e-mail será {}.{}@gmail.com'.format(nome[0], nome[len(nome)-1]))