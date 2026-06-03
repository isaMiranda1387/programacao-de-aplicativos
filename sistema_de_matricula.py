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
        json.dump(alunos, estudantes, indent=4, ensure_ascii=False)
    print("Aluno cadastrado com sucesso!")


def listar(): 
    print("\n--- Lista de Alunos ---") 
    
    if os.path.exists(dados):  
        with open(dados, 'r', encoding='utf-8') as f: 
            alunos = json.load(f) 
    else: 
        alunos = [] 

    if not alunos: 
        print("Nenhum aluno cadastrado.") 

        return

    for aluno in alunos: 
        print(f" Nome: {aluno['nome']} | ID: {aluno['id']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}| Cpf: {aluno['cpf']} ") 

def atualizar(): 
    print("\n--- Atualizar Aluno ---") 

    if not os.path.exists(dados): 
        print("Nenhum aluno cadastrado no sistema.") 

        return 

    with open(dados, 'r', encoding='utf-8') as f: 
        alunos = json.load(f) 
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")
    for aluno in alunos: 
        if aluno['cpf'] == cpf_busca: 
            print(f"Editando dados de: {aluno['nome']}") 

            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) 
            aluno['id'] = input(f"Novo ID ({aluno['id']}): ") or aluno['id'] 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] 
            
            
            with open(dados, 'w', encoding='utf-8') as f:  
                json.dump(alunos, f, indent=4, ensure_ascii=False) 
            print("Dados atualizados com sucesso!") 


def excluir():
    print("\n--- Excluir Aluno ---")

    if not os.path.exists(dados): 
        print("Nenhum aluno cadastrado no sistema.") 

        return 

    with open(dados, 'r', encoding='utf-8') as f:  
        alunos = json.load(f) 
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    nova_lista = [a for a in alunos if a['id'] != id_busca] 
    if len(nova_lista) < len(alunos): 
        with open(dados, 'w', encoding='utf-8') as f: 
        
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) 
        print("Aluno removido com sucesso!")

    else: 
        print("Aluno não encontrado.") 


def menu(): 
    if not os.path.exists(dados): 
        with open(dados, 'w', encoding='utf-8') as f: 
            json.dump([], f) 

    while True: 
        print("\n=== SISTEMA ESCOLAR ===") 
        print("1. Cadastrar Aluno") 
        print("2. Listar Alunos")
        print("3. Atualizar Aluno") 
        print("4. Excluir Aluno")  
        print("5. Sair") 
        
        opcao = input("Escolha uma opção: ") 
        
        if opcao == '1': cadastrar() 
        elif opcao == '2': listar() 
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir() 
        elif opcao == '5': break 
        else: print("Opção inválida!")

menu()         