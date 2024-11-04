frase = input('Digite uma frase: ').upper().strip()

a = frase.count('A')
p = frase.find('A')
f = frase.rfind('A')

print('A letra A aparece {}'.format(a))
print('O primeiro A aparece na posição {}'.format(p))
print('O ultimo A aparece na posição {}'.format(f))