primeiro = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

atual = primeiro
contador = 1

print("Os primeiros 10 termos da progressão aritmética são:")
while contador <= 10:
    print(atual, end=' -> ')
    atual += razao
    contador += 1
print('FIM')
