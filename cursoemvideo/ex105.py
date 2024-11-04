def nota(*n, sit=False):
    s = {}
    s['quant'] = len(n)
    s['maior'] = max(n)
    s['menor'] = min(n)
    s['media'] = sum(n) / len(n)

    if sit:
        if s['media'] >= 7:
            s['situação'] = 'Otima'
        elif 5 <= s['media'] < 7:
            s['situação'] = 'Suficiente'
        else:
            s['situação'] = 'Ruim'
    return s

num = nota(7, 8, 9.5, sit=True)
print(num)

