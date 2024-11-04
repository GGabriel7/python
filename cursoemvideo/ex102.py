def fatorial(n, show=False):
    """fatorial(n, show=False)
    -> Calcula o fatorial de um número
    n: Número a ser calculado
    show: (opcional) Mostra ou não a conta
    return: retorna o fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print('', end=' x ')
            else:
                print('', end=' = ')
    return f

print(fatorial(5, show=True))
#print(fatorial.__doc__)
