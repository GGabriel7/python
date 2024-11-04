expressao = input("Digite uma expressão com parênteses: ")
pilha = []

for char in expressao:
    if char == '(':
        pilha.append('(')

    elif char == ')':
        if len(pilha) > 0:
           pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("EXPRESSAO CORRETA.")
else:
    print("EXPRESSAO INCORRETA.")
