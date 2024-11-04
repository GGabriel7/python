def area(a, b):
    ar = a * b
    print(f'A área de um terreno {a}x{b} é de {ar:.2f}m²')


n1 = float(input('Altura: '))
n2 = float(input('Largura: '))

area(n1, n2)
