import os

dir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(dir, 'cadastro.db')

import sqlite3


def createTable():
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def adicionarUsuario(nome, idade):
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES(?, ?)", (nome, idade))

    conn.commit()
    conn.close()


def listarUsuarios():
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    items = cursor.fetchall()
    conn.close()
    return items


def atualizarUsuario(id, nome=None, idade=None):
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    if nome:
        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (nome, id))
    
    if idade:
        cursor.execute("UPDATE usuarios SET idade = ? WHERE id = ?", (idade, id))

    conn.commit()
    conn.close()


def apagarUsuario(id):
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))

    conn.commit()
    print('Pessoa apagada.')
    conn.close()


def criarJSON():
    import json

    jsonPath = os.path.join(dir, 'usuarios.json')

    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT json_group_array(
            json_object(
                'id', id,
                'nome', nome,
                'idade', idade
            )
        ) AS resultados_json
        FROM usuarios
    ''')

    resultado = cursor.fetchone()[0]
    conn.close()

    if resultado is None:
        resultado = "[]"

    with open(jsonPath, 'w', encoding='utf-8') as arquivo_json:
        json.dump(json.loads(resultado), arquivo_json, ensure_ascii=False, indent=4)
