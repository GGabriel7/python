import sqlite3

class TransactionObject:
    """Classe para gerenciar operações no banco de dados SQLite."""

    def __init__(self, database="clientes.db"):
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute(self, query, params=None):
        if not self.connection:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def persist(self):
        if self.connection:
            self.connection.commit()

    def init_db(self):
        """Cria a tabela de clientes caso ainda não exista."""
        self.connect()
        self.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                sobrenome TEXT,
                email TEXT,
                cpf TEXT
            )
        ''')
        self.persist()
        self.disconnect()

    def insert(self, nome, sobrenome, email, cpf):
        self.connect()
        self.execute(
            "INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?, ?, ?, ?)",
            (nome, sobrenome, email, cpf)
        )
        self.persist()
        self.disconnect()

    def view(self):
        self.connect()
        self.execute("SELECT * FROM clientes")
        rows = self.fetchall()
        self.disconnect()
        return rows

    def search(self, nome="", sobrenome="", email="", cpf=""):
        self.connect()
        self.execute('''
            SELECT * FROM clientes 
            WHERE nome LIKE ? OR sobrenome LIKE ? OR email LIKE ? OR cpf LIKE ?
        ''', (
            f'%{nome}%',
            f'%{sobrenome}%',
            f'%{email}%',
            f'%{cpf}%'
        ))
        rows = self.fetchall()
        self.disconnect()
        return rows

    def delete(self, id):
        self.connect()
        self.execute("DELETE FROM clientes WHERE id=?", (id,))
        self.persist()
        self.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        self.connect()
        self.execute('''
            UPDATE clientes 
            SET nome=?, sobrenome=?, email=?, cpf=? 
            WHERE id=?
        ''', (nome, sobrenome, email, cpf, id))
        self.persist()
        self.disconnect()