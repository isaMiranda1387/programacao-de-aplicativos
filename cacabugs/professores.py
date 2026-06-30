import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O python reclama de "Icorrect number of bindings".
    # Estamos passando a variável, por que ocorre o erro?
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()
    