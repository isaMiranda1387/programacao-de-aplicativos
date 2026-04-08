
usuario = ["Lucas", "Larissa", "Luan", "Lavinia"]
usuarios = []

print("1 - Adicionar usuário")
print("2 - Entrar (login)")
print("3 - Sair")

opcao = input("Escolha uma opção: ")
while opcao != "3": 
    if opcao == "1":
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if usuario in usuarios:
            print("Usuário já existe!")
        else:
            usuarios[usuario] = senha
            print("Usuário cadastrado com sucesso!")

        opcao = input("Escolha uma opção: ")

    elif opcao == "2":
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"Bem-vindo, {usuario}!")
        else:
            print("Usuário ou senha incorretos!")
        
        opcao = input("Escolha uma opção: ")

    elif opcao == "3":
        print("Saindo do sistema.")
    else:
        print("Opção inválida! Tente novamente.")

print("Saindo do sistema.")