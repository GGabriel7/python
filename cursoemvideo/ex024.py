cidade = str(input('Diga o nome da sua cidade: ')).strip()

santo = cidade.split()

if santo[0].upper() == 'SANTO':
    print('Sua cidade, {}, começa com Santo'.format(cidade))
else:
    print('Sua cidade, {}, não começa com Santo'.format(cidade))