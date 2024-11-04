from random import choice
from time import sleep

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')


escolha = str(input('Escolha pedra, papel ou tesoura: ')).strip().upper()

lista = ["PEDRA", "PAPEL", "TESOURA"]

maquina = choice(lista)

if escolha != 'PEDRA' and escolha != 'PAPEL' and escolha != 'TESOURA':
    print('Objeto invalido!')

else:
    print('CARREGANDO.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')

    if escolha == maquina:
        print('EMPATE. Você escolher {} e eu escolhi {}.'.format(escolha, maquina))
    elif(
         (escolha == "PEDRA" and maquina == "TESOURA") or
         (escolha == "PAPEL" and maquina == "PEDRA") or
         (escolha == "TESOURA" and maquina == "PAPEL")
        ):
        print("VOCÊ VENCEU. Você escolher {} e eu escolhi {}.".format(escolha, maquina))

    else:
        print("VOCÊ PERDEU. Você escolher {} e eu escolhi {}.".format(escolha, maquina))
