nome = str(input('Digite seu nome completo:')).strip()

sem = nome.replace(' ', '')
pri = nome.split()

print('Seu nome é {}'.format(nome.upper()))
print('Seu nome é {}'.format(nome.lower()))
print('Seu nome tem {} letras os espaços'.format(len(sem)))
print('Seu nome tem {} no primeiro nome'.format(len(pri[0])))