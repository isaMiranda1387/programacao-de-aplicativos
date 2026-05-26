import json 
import os

dados = 'alunos.json'  

def cadastrar(): 
    if os.path.exists(dados):
        with open(dados, 'r', encoding='utf-8') as estudantes:
            alunos = json.load(estudantes)
    else:
        alunos = []

    novo_aluno = { 
        "id": int(input("ID: ")),
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }

    alunos.append(novo_aluno)

    with open(dados, 'w', encoding= 'utf-8') as estudantes:
        json.dump(novo_aluno, estudantes, indent=4, ensure_ascii=False)
    print("Aluno cadastrado com sucesso!")

cadastrar()


def listar():