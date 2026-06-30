import sqlite3 

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Este bloco quebra ao rodar pela primeira vez em um banco limpo. Por quê? 
    cursor.execute('''
        CREAT TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_serie TEXT,
            id_escola INTEGER, 
            FOREIGN KEY (id_) REFERENCES escolas(id)
        )
    ''')
    conexao.commit()
    conexao.close()