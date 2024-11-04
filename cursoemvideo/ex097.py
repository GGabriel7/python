def mensagem(msg):
    tam = len(msg) + 4
    print(f'{"~"}'*tam)
    print(f'  {msg}')
    print(f'{"~"}'*tam)

mensagem('OLA MUNDO!')
mensagem('Meu nome é Gabriel e tenho 21 anos')
mensagem('1')

mes = input('Escreva algo: ').strip().upper()

mensagem(mes)
