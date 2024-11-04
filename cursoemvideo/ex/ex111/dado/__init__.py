from ex110 import moeda

def moeda(a):
    return f'R${a}'

def resumo(n, q1, q2):
    print(f'''Preço analisado: R${n}
{q1}% do preço: R${moeda.aumentar(n, q1)}
{q2}% do preço: R${moeda.diminuir(n, q2)}
Dobro do preço: R${moeda.dobro(n)}
Metade do preço: R${moeda.metade(n)}''')