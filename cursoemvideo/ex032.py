import calendar

ano = int(input('Escolha um ano: '))

dias = [calendar.monthrange(ano, m)[1] for m in range(1, 13)]

total = sum(dias)

if total == 366:
    print('O ano {} teve um total de {} dias, sendo um ano BISSEXTO'.format(ano, total))
else:
    print('O ano {} teve um total de {} dias, NÃO sendo um ano BISSEXTO'.format(ano, total))