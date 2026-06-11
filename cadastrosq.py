import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_aluno TEXT NOT NULL,
                    telefone_aluno TEXT,
                    turma TEXT,
                    idade_aluno INTEGER,
                    cpf_aluno TEXT UNIQUE NOT NULL
               )''')

nome_aluno = input("Digite seu nome: ")
telefone_aluno = input("Digite o seu número de telefone: ")
turma = input("Digite sua turma: ")
idade_aluno = int(input("Digite sua idade: "))
cpf_aluno = input("Digite seu CPF: ")

comando_inserir = (f'''
                      INSERT INTO alunos(
                      nome_aluno,
                      telefone_aluno,
                      turma,
                      idade_aluno,
                      cpf_aluno
                      )
                      VALUES ('{nome_aluno}', '{telefone_aluno}','{turma}',{idade_aluno},'{cpf_aluno}')''')

cursor.execute(comando_inserir)
conexao.commit()


print("Cadastro realizado com sucesso!")

cursor.execute("SELECT * FROM alunos")

for aluno in cursor.fetchall():
    print(aluno)
             

for aluno in cursor:
    print(f"ID: {aluno[0]}")
    print(f"Nome: {aluno[1]}")
    print(f"Telefone: {aluno[2]}")
    print(f"Turma: {aluno[3]}")
    print(f"Idade: {aluno[4]}")
    print(f"CPF: {aluno[5]}")
    print("-" * 30)    

conexao.close()            