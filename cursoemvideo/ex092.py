from datetime import date

dados = {}
dados['Nome'] = input('Nome: ').title().strip()

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
dados['Idade'] = idade

dados['CTPS'] = int(input('N° da CTPS: (Digite 0 caso não tenha) '))
if dados['CTPS'] != 0:
    dados['Ano da contratação'] = int(input('Ano da contratação: '))
    dados['Salário'] = int(input('Salario: '))
    dados['Aposentadoria'] = date.today().year - dados['Ano da contratação'] + 35 + idade

for k, v in dados.items():
    print(f'{k} é {v}')
