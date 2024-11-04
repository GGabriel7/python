times = ('LIVERPOOL', 'CITY', 'ARSENAL', 'ASTON VILLA', 'TOTTNEHAM',
         'MAN. UNITED', 'WEST HAM', 'BRIGHTON', 'NEWCASTLE', 'WOLVES',
         'CHELSEA', 'BOURNEMOUTH', 'FULHAM', 'CRYSTAL PALACE', 'BRENTFORD',
         'FOREST', 'LUTON TOWN', 'EVERTOM', 'BURNLEY', 'SHEFFIELD', 'PDR')

for seq in times:
        print(f'\n{seq}...............', end ='')
        for letra in seq:
              if letra.upper() in 'AEIOU':
                     print(letra, end = ' ')

print('\n')
