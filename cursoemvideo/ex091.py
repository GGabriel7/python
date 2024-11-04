from random import randint
from operator import itemgetter #Para ordenar em ordem crescente.
from time import sleep

aleatorio = {}

for c in range(1, 5):
    aleatorio[f'Jogador{c}'] = randint(1, 6) #Cria cada jogador no dicionario

for c, a in aleatorio.items():
    print(f'{c} tirou {a}') #Para mostrar o dicionario
    sleep(1)

ranking = []
ranking = sorted(aleatorio.items(), key=itemgetter(1), reverse=True) #Ordenar o dicionario em ordem decrescente dentro da variavel 'ranking'
print('=== RANKING ===')
for b, d in enumerate(ranking):
    print(f'  {b+1}° lugar: {d[0]} tirou {d[1]}.') #Mostrar a ordem
