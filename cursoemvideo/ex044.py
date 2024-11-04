valor = float(input('Qual o valor do produto: R$'))

form_pag = int(input('''Eccolha sua forma de pagamento:
[1] À VISTA no DINHEIRO ou CHEQUE.
[2] À VISTA no CARTÃO.
[3] Em até 2X no CARTÃO.
[4] 3X ou MAIS no CARTÃO.\n'''))

if form_pag == 1:
    print('O valor a pagar no produto será R${}'.format(valor - (valor * 0.1)))

elif form_pag == 2:
    print('O valor a pagar no produto será R${}'.format(valor - (valor * 0.05)))

elif form_pag == 3:
    parcelas = int(input('Quantas parcelas? '))
    valorparcelas = valor / parcelas

    if parcelas <= 0:
        print('Parcelamento INVALIDO')

    elif 1 == parcelas == 2:
        print('O valor a pagar no produto será R${}, em {} vezes de R${}'.format(valor, parcelas, valorparcelas))

    else:
        print('Esse número ultrapassa as 2X. Em {} parcelas, o valor será de R${} por mês. O valor a pagar no produto será R${}'.format(parcelas, valorparcelas, (valor * 0.2) + valor))

elif form_pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    valorparcelas = (valor * 0.2 + valor) / parcelas

    if parcelas >= 3:
        print('Em {} parcelas, o valor será de R${} por mês. O valor a pagar no produto será R${}'.format(parcelas, valorparcelas, (valor * 0.2) + valor))

    else:
        print('Essa parcela está abaixo de 3X, então valor a pagar no produto será R${}'.format(valor))

else:
    print('Não há essa opção!')
