primeiro = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

atual = primeiro
contador = 1

total = 0
mais = 10

print("Os primeiros 10 termos da progressão aritmética são:")
while contador <= 10:
    print(atual, end=' -> ')
    atual += razao
    contador += 1
print('FIM')

esc = 1

while esc >= 1:
    esc = int(input('Escolha mais quantos termos você quer ver nessa prograssão (Digite [0] para sair): '))

    atual = primeiro
    contador = 1

    print("Os primeiros {} termos da progressão aritmética são:".format(esc))
    while contador <= esc:
        print(atual, end=' -> ')
        atual += razao
        contador += 1
    print('FIM')
