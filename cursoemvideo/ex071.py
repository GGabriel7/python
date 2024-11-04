print('=' * 8)
print('BANCO GB')
print('=' * 8)

valor = int(input('DIGA SEU VALOR PARA SACAR: '))

cedula = 50
totalcedula = 0
total = valor

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1

    else:
        if totalcedula > 0:
            print(f'{totalcedula} cédula de {cedula}R$')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0

        if total == 0:
            break
