import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON; ")

    # Se o id_prof não existir, ocorre um IntegrityError.
    # Se o erro acontecer, o que ocorre com a liha conexao.close()?
    cursor.execute('''
        CREAT TABLE IF NOT EXIXTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT
        )
    ''')
    