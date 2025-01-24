import os

dir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(dir, 'exemplo.db')

import sqlite3

conn = sqlite3.connect(dbPath)

conn.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             email TEXT NOT NULL
             );
''')

conn.execute("INSERT INTO usuarios (nome, email) VALUES ('Drica', 'drica@email.com');")
conn.execute("INSERT INTO usuarios (nome, email) VALUES ('Gabriel', 'gabriel@email.com');")

conn.commit()
conn.close()