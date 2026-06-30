import sqlite3 

def inicializar_banco():
    conexao = sqlite3.conecct('sistema_escola.db')
    cursor = conexao.cursor

    cursor.execute('''
    CREAT TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL 
    )
    ''')
    # o banco de dados não está salvando as alterações. Por quê? 
    conexao.close()