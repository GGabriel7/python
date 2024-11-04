from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if 18 <= idade < 65:
        return f'Com idade {idade}: Voto Obrigtório'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Com idade {idade}: Voto Opcional'
    else:
        return f'Com idade {idade}: Não vota'

nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
