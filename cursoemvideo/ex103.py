def ficha(j='', g=0):
    if g.isdigit():
        g = int(g)
    else:
        g = 0
    if j == '':
        j = '<desconhecido>'
    print(f'O jogador {j} fez o toal de {g} gols.')

nome = input('Nome do jogador: ').strip().title()
gols = input('Total de gols: ')

ficha(nome, gols)
