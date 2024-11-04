alunos = []

while True:
    nome = [input('NOME: ').upper()]

    nota1 = float(input('1° NOTA: '))
    nome.append(nota1)
    nota2 = float(input('2° NOTA: '))
    nome.append(nota2) #Adicona as notas na lista NOME

    alunos.append(nome) #Adiciona a lista NOME na lista ALUNOS

    while True: #SAIR OU NÃO DO PROGRAMA
        esc = input('CONTINUAR? [S/N] ').strip().upper()
        if esc == 'S':
            break
        if esc == 'N':
            break
    if esc == 'N':
        break

print('-=' * 10)
print(f'{"N°":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 20)

for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10} {(a[1] + a[2]) / 2:>8}') #MOSTRA TODOS OS ALUNOS E AS MEDIAS
print('-=' * 10)

while True:
    esco = int(input('Mostrar nota de qual ALUNO? (999 encerra o programa) '))

    if esco == 999:
        break

    for a, c in enumerate(alunos):
        if a == esco:
            print('-' * 20)
            print(f'O(a) aluno(a) {c[0]} tirou as notas {c[1:]}') #MOSTRA UM ALUNO ESPECIFICO
            print('-' * 20)
            break
