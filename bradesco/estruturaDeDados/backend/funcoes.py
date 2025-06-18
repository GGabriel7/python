import sqlite3 as sql

class TransactionObject:
    database = "clientes.db"
    connection = None
    cursor = None
    connected = False
    
    def connect(self):
        TransactionObject.connection = sql.connect(TransactionObject.database)
        TransactionObject.cursor = TransactionObject.connection.cursor()
        TransactionObject.connected = True
    
    
    def disconnect(self):
        TransactionObject.connection.close()
        TransactionObject.connected = False
        
    
    def execute(self, query, params=None):
        if TransactionObject.connected:
            if params is None:
                TransactionObject.cursor.execute(query)
            else:
                TransactionObject.cursor.execute(query, params)
            return True
        else:
            return False
        
    
    def fetchall(self):
        return TransactionObject.cursor.fetchall()

    
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.connection.commit()
            return True
        else:
            return False
    
    
    def initDB():
        trans = TransactionObject()
        trans.connect()
        
        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()
        
    
    def insert(nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()
        
    
    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    
    def search(nome="", sobrenome="", email="", cpf=""):
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    
    def delete(id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.persist()
        trans.disconnect()
        
    
    def update(id, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()
        
    
TransactionObject.initDB()