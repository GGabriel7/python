peso = float(input('Qual seu peso(em quilos)? '))
altura = float(input('E sua altura (em cm)? '))

imc = peso / ((altura / 100) ** 2)

if imc < 18.5:
    print('Seu IMC de {:.2f}, faz você estar ABAIXO DO PESO'.format(imc))

elif 18.5 <= imc <= 25:
    print('Seu IMC de {:.2f}, faz você estar com o PESO IDEAL'.format(imc))

elif 25.0 < imc <= 30:
    print('Seu IMC de {:.2f}, faz você estar SOBREPESO'.format(imc))

elif 30.0 < imc <= 40:
    print(f'Seu IMC de {imc}, faz você estar com OBESIDADE')

elif imc > 40:
    print(f'Seu IMC de {imc}, faz você estar com OBESIDADE MÓRBIDA')
