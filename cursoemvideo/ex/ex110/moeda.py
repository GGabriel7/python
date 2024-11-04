def aumentar(n, q, form=False):
    if form:
        return f'R${n + (n * (q/100))}'
    return n + (n * (q/100))

def diminuir(n, q, form=False):
    if form:
        return f'R${n - (n * (q/100))}'
    return n - (n * (q/100))

def dobro(a, form=False):
    if form:
        return f'R${a * 2}'
    return a * 2

def metade(a, form=False):
    if form:
        return f'R${a / 2}'
    return a / 2

def moeda(a):
    return f'R${a}'

def resumo(n, q1, q2):
    print(f'''Preço analisado: R${n}
{q1}% do preço: R${aumentar(n, q1)}
{q2}% do preço: R${diminuir(n, q2)}
Dobro do preço: R${dobro(n)}
Metade do preço: R${metade(n)}''')