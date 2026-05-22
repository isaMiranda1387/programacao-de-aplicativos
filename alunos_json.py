import json # o import json serve para o código nao dar erro, ou seja, ele serve para o código ser lido e escrito
import os # ele permite que navegue pelas pastas e os arquivos

BANCO_DADOS = 'alunos.json' # aqui foi criado uma variavel que guarda o nome do arquivo

def cadastrar(): # aqui foi feito um def, para criar uma função para conseguir cadastrar
    print("\n--- Novo Cadastro ---") # esse print foi gerado para aparecer de uma forma organizada no terminal (novo cadastro)
    
    if os.path.exists(BANCO_DADOS): # esse if seve para ver SE o arquivo existe 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # o with open serve para abrir o arquivo
            alunos = json.load(f) # aqui ele esta lendo os dados do arquivo
    else: # caso o if nao seja correspondido, criamos um else, para ser a resposta contraria imediata
        alunos = [] # é a resposta exibida do else criando uma lista

    novo_aluno = { # cria um objeto chamado novo_aluno 
        "nome": input("Nome: "), # pede o nome 
        "telefone": input("Telefone: "), # pede o telefone
        "turma": input("Turma: "), # peda a turma
        "idade": int(input("Idade: ")), # pede a idade, e usa o int para tranformar num numero inteiro
        "cpf": input("CPF: ") # pede o cpf
    } # fecha o objeto
    
    alunos.append(novo_aluno) # o alunos.append, serve para adcionar um novo aluno na lista alunos

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre o arquivo novamente, o w serve para sobrescrever
        json.dump(alunos, f, indent=4, ensure_ascii=False) # salva os dados dentro do arquivo
        
    print("Aluno cadastrado com sucesso!") # esse print serve para mostrar uma mensagem no terminal

def listar(): # esse def foi para criar a função listar 
    print("\n--- Lista de Alunos ---") # esse print serve para mostrar uma mensagem no terminal, o \n serve para quebrar linha

    
    if os.path.exists(BANCO_DADOS): #esse if esta verificando se o arquivo existe  
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # o with esta abrindo, e o encoding= 'utf-8' serve para formartar 
            alunos = json.load(f) # carrega os alunos
    else: # aqui serve para quado o if nao for correspondido
        alunos = [] # cria uma lista se o arquivo nao existir (else)

    if not alunos: # esta verificando se a lista esta vazia
        print("Nenhum aluno cadastrado.") # esse print serve para mostrar uma mensagem no terminal

        return # o return serve para encerrar a função

    for aluno in alunos: # percorre cada aluno dentro da lista 
        print(f" Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # esse print serve para mostrar uma mensagem no terminal, usando f-string


def atualizar(): # cria uma função para atualizar 
    print("\n--- Atualizar Aluno ---") # esse print serve para mostrar uma mensagem no terminal

    if not os.path.exists(BANCO_DADOS): # o if esta vereficando se o arquivo existe
        print("Nenhum aluno cadastrado no sistema.") # esse print serve para mostrar uma mensagem no terminal, o \n serve para quebrar a linha 

        return # o return serve para encerrar a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # aqui esta abrindo o arquivo e formatando
        alunos = json.load(f) # aqui esta carregando os dados do arquivo
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # aqui ele esta pedindo o cpf do aluno, usando o int e input
    
    for aluno in alunos: # percorre os alunos 
        if aluno['cpf'] == cpf_busca: # aqui esta verificando se o cpf do aluno corresponde com o digitado
            print(f"Editando dados de: {aluno['nome']}") # esse print serve para mostrar uma mensagem no terminal

            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # se digital algo novo, ira atualizar as informações 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] # se digital algo novo, ira atualizar as informações
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # se digital algo novo, ira atualizar as informações
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) # se digital algo novo, ira atualizar as informações
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] # se digital algo novo, ira atualizar as informações
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # o with esta abrindo, e o encoding= 'utf-8' serve para formartar 
                json.dump(alunos, f, indent=4, ensure_ascii=False) # aqui esta salvando as informações que foram alteradas
            print("Dados atualizados com sucesso!") # esse print serve para mostrar uma mensagem no terminal

            return # o return aqui esta servindo para encerrar a função 
            
    print("Aluno não encontrado.") # esse print serve para mostrar uma mensagem no terminal


def excluir(): # aqui esse def esta criando a função excluir
    print("\n--- Excluir Aluno ---") # esse print serve para mostrar uma mensagem no terminal

    if not os.path.exists(BANCO_DADOS): # esta verificando se o rquivo existe, caso não existir vai exibir print
        print("Nenhum aluno cadastrado no sistema.") # esse print serve para mostrar uma mensagem no terminal

        return # encerra a função 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  # aqui esta abrindo o arquivo e formatando
        alunos = json.load(f) # aqui esta carregando os dados do arquivo
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # aqui ele esta pedindo para o usario digitar o cpf, assim ele salvo dentro da variavel e retorna o texto por conta do string e input
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # aqui esta criando uma nova lista sem alunos com o cpf digitado
    
    if len(nova_lista) < len(alunos): # aqui esta verificando se o aluno foi removido
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # aqui esta abrindo o arquivo e formatando
        
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # aqui esta salvando numa nova lista 
        print("Aluno removido com sucesso!") # esse print serve para mostrar uma mensagem no terminal

    else: # caso nao corresponda com o if, sera exibido o print 
        print("Aluno não encontrado.") # esse print serve para mostrar uma mensagem no terminal


def menu(): # esta criando a função menu
    if not os.path.exists(BANCO_DADOS): # aqui esta verificando se o arquivo existe
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # aqui esta abrindo o arquivo e formatando
            json.dump([], f) # caso nao exista, vai criar um json vazio

    while True: # aqui vai criar uma reptição infinita ate escolher sair
        print("\n=== SISTEMA ESCOLAR ===") # esse print serve para mostrar uma mensagem no terminal
        print("1. Cadastrar Aluno") # esse print serve para mostrar uma mensagem no terminal
        print("2. Listar Alunos") # esse print serve para mostrar uma mensagem no terminal
        print("3. Atualizar Aluno") # esse print serve para mostrar uma mensagem no terminal
        print("4. Excluir Aluno") # esse print serve para mostrar uma mensagem no terminal
        print("5. Sair") # esse print serve para mostrar uma mensagem no terminal
        
        opcao = input("Escolha uma opção: ") # aqui mostra a opção do menu
        
        if opcao == '1': cadastrar() # aqui chama um cadastro
        elif opcao == '2': listar() # aqui chama uma listagem
        elif opcao == '3': atualizar() # aqui chama uma atualização
        elif opcao == '4': excluir() # aqui chama exclusão
        elif opcao == '5': break # aqui sai do programa
        else: print("Opção inválida!") # esse print serve para mostrar uma mensagem no terminal

menu() # esta chamando a funçao

