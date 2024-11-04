dados = {}
lista = [[], []]
idades = 0

while True:
    dados['Nome'] = input('Nome: ').strip().title()#NOME

    while True:
        dados['Sexo'] = input('Sexo[M/F]: ').strip().upper()#SEXO
        if dados['Sexo'] == 'M' or dados['Sexo'] == 'F':
            if dados['Sexo'] == 'F':
                lista[0] = dados.copy()
            break

    dados['Idade'] = int(input('Idade: '))

    idades += dados['Idade']

    lista.append(dados.copy())

    media = idades / (len(lista)-2)

    if dados['Idade'] >= media:
         lista[1] = dados.copy()

    while True:
        esc = input('Continuar[S/N]? ').strip().upper()
        if esc == 'N' or esc == 'S':
            break
    if esc == 'N':
        break

print('=' * 30)
print(f'- O grupo tem {len(lista)-2} pessoa(s).')

print(f'- A media de idade das pessoas é {media:.2f}')

print(f'- As mulheres cadastradas foram: {lista[0]}')

print(f'- Lista das pessoas que estão com idade acima da média: {lista[1]}')
