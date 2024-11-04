somaidade = 0
idadehomemvelho = 0
nomevelho = 0
mulher20 = 0

for n in range(1, 5):
    print('------ {}° PESSOA ------'.format(n))

    nome = str(input('Nome da pessoa {}: '.format(n))).strip().upper()
    idade = int(input('Idade da pessoa {}: '.format(n)))
    sexo = str(input('Sexo:\n[M] Masculino\n[F] Feminio:\n'.format(n))).strip().upper()

    somaidade += idade

    if n == 1 and sexo in 'M':
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in 'M' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomevelho = nome

    if sexo in 'F' and idade > 20:
        mulher20 += 1

print('Média de idade: {}'.format(somaidade / 4))
print('O nome do homem mais velho é {}, ele tem {} anos'.format(nomevelho, idadehomemvelho))
print('{} mulheres tem mais de 20 anos.'.format(mulher20))
