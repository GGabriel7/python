import sqlite3 # importa a biblioca já integrada ao python para utilizar o SQLlite
import os #

dir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(dir, 'arquivoTeste.db')

conn = sqlite3.connect(dbPath) #Conecta ao banco de dados
cursor = conn.cursor() #Cria um cursar para criar, modicar ou excluir no banco de dados com .execute()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tabela_teste ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
''')
# CREATE TABLE = Cria a tabela
# IF NOT EXISTS = Caso não exista
# id, name e idade = as tabelas do db
# Integer e TEXT = Tipos dos dados (inteiro e texto)
# PRIMARY KEY = Identificador das colunas

conn.commit() #salva as alterações durante a conexão com o bd
conn.close() #fecha a conexão com o db


def adicionar(nome, idade):
    dir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(dir, 'arquivoTeste.db')

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tabela_teste (nome, idade)
        VALUES (?, ?)
    ''', (nome, idade))
    # INSERT INTO adiciona dados a determinada tabela
    # VALUES serão os determinados valores a serem adicionados
    
    conn.commit()
    print("Pessoa adicionado com sucesso.")
    conn.close()


def listar():
    dir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(dir, 'arquivoTeste.db')

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tabela_teste')
    # SELECT * FROM selecioa toda a tabela
    # Para selecionar um dado especifico, altere o * para um dado especifico

    items = cursor.fetchall() # Busca a tabela seleciona e a retorna
    
    if items: 
        for item in items:
            print(f'ID: {item[0]} | Nome: {item[1]} | Idade: {item[2]}')
    else:
        print("Nunhuma pessoa cadastrado.")

    conn.close()


def atualizarIdade(idade, id):
    dir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(dir, 'arquivoTeste.db')

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('UPDATE tabela_teste SET idade = ? WHERE id = ?', (idade, id)) 
    # UPDATE atualiza algum determinado dado de uma tabela utilizando o ID para o identificar

    conn.commit()
    print("Idade atualizada com sucesso!")
    conn.close()

def atualizarNome(nome, id):
    conn = sqlite3.connect('comandosSQL/arquivoTeste.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE tabela_teste SET nome = ? WHERE id = ?', (nome, id))

    conn.commit()
    print("Nome atualizado com sucesso!")
    conn.close()



def apagar(id):
    dir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(dir, 'arquivoTeste.db')

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tabela_teste WHERE id = ?', (id,))
    # DELETE deleta 
    
    conn.commit()
    print('Pessoa apagada.')
    conn.close()


def menu():
    while True:
        print("\n=== Sistema de Cadastro de Pessoas ===")
        print("1. Adicionar Pessoa")
        print("2. Listar Pessoas")
        print("3. Excluir Pessoa")
        print("4. Atualizar idade da Pessoa")
        print("5. Atualizar nome da Pessoa")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Nome: ")
            autor = input("Idade: ")
            adicionar(titulo, autor)

        elif escolha == "2":
            listar()

        elif escolha == "3":
            id = input("Escolha o ID para ser exluido: ")
            apagar(id)

        elif escolha == "4":
            id = input("Qual ID você quer alterar? ")
            idade = input("Qual idade correta? ")
            atualizarIdade(idade, id)

        elif escolha == "5":
            id = input("Qual ID você quer alterar? ")
            nome = input("Qual nome correto? ")
            atualizarNome(nome, id)

        elif escolha == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()