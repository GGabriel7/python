num = int(input('Até qual sequencia voce quer ver? '))

f = [0, 1]

while len(f) < num:
    f.append(f[-1] + f[-2])
print(f)
print('FIM!')
