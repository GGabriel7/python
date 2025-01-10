from area import Retangulo
import math

while True:
    pisoA = float(input('Digite um lado do piso: '))
    pisoB = float(input('Digite o outro lado do piso: '))

    piso = Retangulo(pisoA, pisoB)

    azA = ﬂoat(input('Digite o lado do azulejo: '))
    azB = ﬂoat(input('Digite o outro lado do azulejo: '))

    azulejo = Retangulo(azA, azB)

    areaPiso = piso.area()
    areaAz = azulejo.area()

    quantAz = areaPiso / areaAz

    if areaPiso % areaAz == 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {quantAz}')
    else:
        print(f'A quantidade mínima de azulejos para preencher o piso pe de {math.ceil(quantAz)}')