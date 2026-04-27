def senha_valida (senha_aprovada):
    while len(senha_aprovada) < 6:
        senha_aprovada = input("Digite a senha")
        if len(senha_aprovada) >= 6:
            print("Senha válida")
            return True
        else:
            print("Senha inválida, mínimo 6 caracteres")
            return False

senha_usuario = int(input("Digite sua senha: "))
msg = senha_valida(senha_usuario)  
print(msg)     
