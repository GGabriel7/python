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