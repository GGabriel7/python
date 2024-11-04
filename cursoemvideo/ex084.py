pessoa = []
pessoas = []

maior = float('-inf')
menor = float('inf') #declarar maior e menor peso

while True:
    pessoa.append(input('NOME: ').upper().strip())
    pessoa.append(float(input('PESO: ')))

    if pessoa[1] >= maior:
        maior = pessoa[1]
    if pessoa[1] <= menor:
        menor = pessoa[1] #Ver qual o menor e o maior

    pessoas.append(pessoa[:]) #Criar uma cópia da lista PESSOA na lista PESSOAS

    while True:
        esc = input('CONTINUAR? [S/N]').upper().strip()
        if esc == 'S':
            break
        if esc == 'N':
            break
    if esc == 'N':
        break

    pessoa.clear()

print(f'{len(pessoas)} pessoa(s) foram cadastradas.')

print(f'O maior peso foi {maior}Kg. São eles: ', end = '')#Mostrar o maior peso
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end = '') #Mostrar a ou as pessoas com o MAIOR peso

print(f'\nO menor peso foi {menor}Kg. São eles ', end = '')#Mostrar o menor peso
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end = '')#Mostrar a ou as pessoas com o MENOR peso
print()
