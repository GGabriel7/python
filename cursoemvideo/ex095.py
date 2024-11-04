time = []
jogador = {}
partidas = []

while True:
    jogador.clear()#Limpa os dados

    jogador['Nome'] = input('Nome do jogador: ').title().strip()#pega o nome e coloca em um dicionario ('Nome')

    total = int(input(f'Quantas partidas {jogador["Nome"]} fez: '))#para pegar o total do jogos

    partidas.clear()#irá limpar os dados das partidas

    for c in range(1, total+1): #lopping para colocar os gols em cada partida
        partidas.append(int(input(f'Gols na partida {c}: ')))

    jogador['Gols'] = partidas[:] #coloca as copias ([:]) dos gols declarados no looping anterior em outro dicionario ('Gols')
    jogador['Total de gols'] = sum(partidas) #faz a soma dos gols declarados e coloca em outro dicionario ('Total de gols')

    time.append(jogador.copy()) #atribui uma copia do dicionario na lista 'time'

    while True:#continuar ou não
        esc = input('Continuar[S/N]? ').strip().upper()
        if esc == 'N' or esc == 'S':
            break
    if esc == 'N':
        break

print('--' * 20)

print('Cod. ', end='')

for i in jogador.keys():#Para mostrar as chaves dos dicionarios
    print(f'{i:<13} ', end = '')
print()

print('--' * 20)

for k, v in enumerate(time):
    print(f'{k:>3} ', end = '') #"criar" um codigo para cada jogador
    for d in v.values():# Para mostrar os valores d dicionari
        print(f'{str(d):<15}', end = '')
    print()

print('-' * 30)

while True:#para mostrar os dados de um por vez
    busca = int(input('Qual jogador você quer ver? (999 encerra) Cod: '))
    if busca == 999:
        break

    if 1 >= busca >= len(time):
        print('ERRO! Não há jogador com esse Cod.')

    else:
        print(f'== JOGADOR {time[busca]["Nome"]} ==')
        for i, g in enumerate(time[busca]["Gols"]): #para mostrar um jogador da lista por vez
            print(f'No jogo {i+1} fez {g}')
        print('--' * 20)
