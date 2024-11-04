from random import choice

a = input('1° Aluno: ')
b = input('2° Aluno: ')
c = input('3° Aluno: ')
d = input('4° Aluno: ')

lista = [a, b, c, d]
sorteio = choice(lista)

print('O aluno escolhido é: {}'.format(sorteio))
