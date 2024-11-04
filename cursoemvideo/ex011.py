a = float(input('Qual a altura da parede? \n'))
l = float(input('Qual a largura da parede? \n'))

ar = l * a
t = ar / 2

print('Serãp necessário {} baldes de tinta para pintar sua parede de {}m2 de area'.format(t, ar))
print(f'Serãp necessário {t} baldes de tinta para pintar sua parede de {ar}m2 de area')