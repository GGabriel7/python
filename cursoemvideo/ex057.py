r = input('Qual seu sexo?\n[F] Feminino\n[M] Masculino\n').strip().upper()

while 'M' != r != 'F':
        r = input('DADO INVÁLIDO! Por favor, informe seu sexo: ').strip().upper()

if r == 'M':
        r = 'masculino'
else:
        r = 'feminio'

print('Obrigado! Sexo {} registrado com sucesso.'.format(r))
