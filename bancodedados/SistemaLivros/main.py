import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# CRIANDO TABELAS
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER NOT NULL,
        usuario_id INTEGER NOT NULL,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        FOREIGN KEY (livro_id) REFERENCES livros (id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
''')

print("Banco de dados configurado com tabelas relacionadas!")
conn.commit()
conn.close()


# PREECHENDO TABELAS
def adicionarLivro(titulo, autor, ano):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano))
    
    conn.commit()
    print("Livro adicionado com sucesso")
    conn.close()


def adicionaUsuario(nome, email):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO usuarios (nome, email)
    VALUES (?, ?)
    ''', (nome, email))

    conn.commit()
    print("Usuário adicionado com sucesso!")
    conn.close()


def registrarEmprestimo(livro_id, usuario_id, data_emprestimo):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo)
    VALUES (?, ?, ?)
    ''', (livro_id, usuario_id, data_emprestimo))

    conn.commit()
    print("Empréstimo registrado com sucesso!")
    conn.close()


# LISTAR TABELAS
def listarLivros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    if livros:
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]}")
    else:
        print("Nenhum livro cadastrado.")

    conn.close()


def listarUsuario():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
    else:
        print("Nenhum usuário cadastrado.")

    conn.close()


def listarEmprestimos():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT e.id, l.titulo, u.nome, e.data_emprestimo, e.data_devolucao
    FROM emprestimos e
    JOIN livros l ON e.livro_id = l.id
    JOIN usuarios u ON e.usuario_id = u.id
    ''')
    emprestimos = cursor.fetchall()

    if emprestimos:
        for emprestimo in emprestimos:
            print(f"ID: {emprestimo[0]} | Livro: {emprestimo[1]} | Usuário: {emprestimo[2]} | Data Empréstimo: {emprestimo[3]} | Data Devolução: {emprestimo[4]}")
    else:
        print("Nenhum empréstimo registrado.")
    
    conn.close()


def menu():
    while True:
        print("\n=== Sistema de Cadastro de Livros ===")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Adicionar Usuário")
        print("4. Listar Usuários")
        print("5. Registrar Emprestimo")
        print("6. Listar Emprestimos")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            adicionarLivro(titulo, autor, ano)

        elif escolha == "2":
            listarLivros()

        elif escolha == "3":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionaUsuario(nome, email)

        elif escolha == "4":
            listarUsuario()

        elif escolha == "5":
            idLivro = input("ID do Livro: ")
            idUsuario = input("ID do Usuário: ")
            data = input("Data do Emprestimo: ")
            registrarEmprestimo(idLivro, idUsuario, data)
        
        elif escolha == "6":
            listarEmprestimos()

        elif escolha == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()