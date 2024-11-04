times = ('LIVERPOOL', 'CITY', 'ARSENAL', 'ASTON VILLA', 'TOTTNEHAM',
         'MAN. UNITED', 'WEST HAM', 'BRIGHTON', 'NEWCASTLE', 'WOLVES',
         'CHELSEA', 'BOURNEMOUTH', 'FULHAM', 'CRYSTAL PALACE', 'BRENTFORD',
         'FOREST', 'LUTON TOWN', 'EVERTON', 'BURNLEY', 'SHEFFIELD')

print(f'Tabala atual: {times}\n')
print('-=' * 42, '\n')

print(f'G4: {times[:4]}\n')
print('-=' * 42, '\n')

print(f'Z3: {times[-3:]}\n')
print('-=' * 42, '\n')

print(f'ORDEM ALFABETICA: {sorted(times)}\n')
print('-=' * 42, '\n')

for p in enumerate(times):
    if p[1] == 'WEST HAM':
        print(f'O {times[6]} está na {p[0] + 1}° colocação.')

print(f'O {times[6]} está na {times.index("WEST HAM") + 1}° colocação. ')
