aluno = {}
aluno['NOME'] = str(input('NOME DO ALUNO: ')).upper()
aluno['NOTA'] = float(input('MÉDIA DO ALUNO: '))

if aluno['NOTA'] >= 7:
    aluno['SITUACAO'] = 'APROVADO'
elif 5 <= aluno['NOTA'] < 7:
    aluno['SITUACAO'] = 'RECUPERAÇÃO'
else:
    aluno['SITUACAO'] = 'REPROVADO'

print()
for c, v in aluno.items():
        print(f'{c} é igual a {v}.')
