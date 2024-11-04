dados = {}
dados['Nome'] = input('Nome do jogador: ').title().strip()
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} fez: '))

gols= []
for c in range(1, dados['Partidas']+1):
    gol = int(input(f'Gols na partida {c}: '))
    gols.append(gol)

dados['Total'] = sum(gols)
dados['Gols'] = gols[:]

print('-=' * 10)
print(dados)
print('-=' * 10)

for a, b in dados.items():
    print(f'O campo {a} tem valor {b}')

print('-=' * 10)

print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partida(s).')

for t, g in enumerate(gols):
    print(f'    ==> Na partida {t+1}, fez {g} gol(s)')

print(f'Fez o total de {dados["Total"]} gols.')
