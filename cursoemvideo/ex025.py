nome = str(input('Digite seu nome completo: ')).strip()

silva = nome.upper().split()

if 'SILVA' in silva[0:]:
    print('Seu nome {} tem silva'.format(nome))
else:
    print('Seu nome {} não tem silva.'.format(nome))