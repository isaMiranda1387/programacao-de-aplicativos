import json, os
def criar_arquivo():
    open("alunos.json" , 'w').close()

def criar_usuario():     
    cpf = int(input("Digite seu cpf abaixo: "))
    nome = input("Digite seu nome abaixo: ")
    telefone = int(input("Digite seu telefone abaixo: "))
    turma = int(input("Digite sua turma abaixo: "))
    idade = int(input("Digite sua idade  abaixo: "))

    aluno = {
        "cpf": cpf,
        "nome" : nome,
        "telefone" : telefone,
        "turma" : turma,
        "idade" : idade
        }
    

    if os.path.getsize("alunos.json") == 0:
        print("Arquivo vazio")
        dados = []

    else:
        with open("alunos.json", "r") as arquivo:
            dados = json.load(arquivo)


    dados.append(aluno)


    with open("alunos.json" , 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
        print(f"Aluno criado com sucesso!")
    
criar_usuario()