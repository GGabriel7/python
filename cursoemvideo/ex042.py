ladoa = float(input('Primeiro lado: '))
ladob = float(input('Segundo lado: '))
ladoc = float(input('Terceriro lado: '))

if ladoa > ladob + ladoc or ladob > ladoa + ladob or ladoc > ladoa + ladob:
    print('Isso não pode formar um triangulo.')
else:
    if ladoa == ladob == ladoc:
        print('Equilátero')
    elif ladoa == ladob or ladob == ladoc or ladoc == ladoa:
        print('Escaleno')
    else: # ladoa != ladob != ladoc != ladoa
        print('Isosceles')
