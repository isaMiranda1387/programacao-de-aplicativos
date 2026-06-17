import sqlite3
def cadastrar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_professor TEXT NOT NULL,
                        telefone_professor TEXT,
                        materia TEXT,
                        idade_professor INTEGER,
                        cpf_professor TEXT UNIQUE NOT NULL,
                        salario_professor REAL NOT NULL,
                        escola TEXT NOT NULL
                )''')

    nome_professor = input("Digite seu nome: ")
    telefone_professor = input("Digite o seu número de telefone: ")
    materia = input("Digite sua materia: ")
    idade_professor = int(input("Digite sua idade: "))
    cpf_professor = input("Digite seu CPF: ")
    salario_professor = float(input("Digite o seu salário: "))
    escola_aula = input("Digite o nome da escola que você da aula atuamente: ")

    comando_inserir = (f'''
                        INSERT INTO professores(
                        nome_professor,
                        telefone_professor,
                        materia,
                        idade_professor,
                        cpf_professor,
                        salario_professor,
                        escola  
                    )
                        VALUES ('{nome_professor}', '{telefone_professor}','{materia}',{idade_professor},'{cpf_professor}',
                            {salario_professor},'{escola_aula}')''')

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

def listar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute(''' SELECT * FROM professores''')
    todos_professores = cursor.fetchall()

    if not todos_professores:
        print("Nenhum professor cadastrado! ")

        print("=== Lista de Professores ===")

    for professor in todos_professores: 
        print(f"ID: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print(f"Telefone: {professor[2]}")
        print(f"Materia: {professor[3]}")
        print(f"Idade: {professor[4]}")
        print(f"CPF: {professor[5]}")
        print(f"Salario: {professor[6]}")
        print(f"Escola: {professor[7]}")
        print("-" * 30)

        conexao.close()

def atualizar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    
    id_professor = int(input("Digite o seu ID: "))

    cursor.execute(f''' SELECT * FROM professores WHERE id = {id_professor} ''')
    
    todos_professores = cursor.fetchall()
    if not todos_professores:
        print("Nenhum professor encontrado! ")
        conexao.close()
        return
    
    else:
        listar()

        nome_atualizado = input("Atualize seu nome: ")
        cpf_atualizado = input("Atualize seu CPF: ")
        telefone_atualizado = input("Atualize seu telefone: ")
        materia_atualizada = input("Atualize sua matéria: ")
        idade_atualizada = int(input("Atualize sua idade: "))
        salario_atualizado = float(input("Atualize seu salário: "))
        escola_atualizada = input("Atualize o nome da escola: ")

        cursor.execute(f'''
                       UPDATE professores
                        SET nome_professor = '{nome_atualizado}', 
                        cpf_professor = '{cpf_atualizado}', 
                        telefone_professor = '{telefone_atualizado}', 
                        materia = '{materia_atualizada}', 
                        idade_professor = {idade_atualizada}, 
                        salario_professor = {salario_atualizado}, 
                        escola = '{escola_atualizada}' 
                        WHERE ID = {id_professor} ''')
                            
    conexao.commit()
    print(" Dados alterados ")

    conexao.close()

def deletar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    listar()

    id_professor = int(input("Digite o ID que deseja deletar: "))

    cursor.execute(f'''DELETE FROM professores WHERE id = {id_professor}''')

    conexao.commit()
    print("ID deletado: ")

    conexao.close()

def menu():

    while True:    
        print("\n --- TABELA DE PROFESSORES ---")
        print("\n === SISTEMA ESCOLAR === ")
        print("1. Cadastrar professor ")
        print("2. Listar professor ")
        print("3. Atualizar professor ")
        print("4. Deletar professor ")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1': cadastrar()
        elif opcao == '2': listar() 
        elif opcao == '3': atualizar()
        elif opcao == '4': deletar()
        elif opcao == '5': break

        else:
            print("Opção inválida.")
menu()
