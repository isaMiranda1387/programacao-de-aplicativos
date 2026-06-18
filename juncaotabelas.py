def listar_professor_com_alunos():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_professor = int(
        input("Digite o ID do professor: ")
    )

    cursor.execute('''
        SELECT
            professores.nome_professor,
            alunos.nome_aluno
        FROM professores
        LEFT JOIN alunos
        ON professores.id = alunos.id_professor
        WHERE professores.id = ?
    ''', (id_professor,))

    resultados = cursor.fetchall()

    print("\n=== ALUNOS DO PROFESSOR ===")

    for dado in resultados:
        print(
            f"Professor: {dado[0]} | Aluno: {dado[1]}"
        )

    conexao.close()