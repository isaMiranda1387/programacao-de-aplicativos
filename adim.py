usuario = input("Qual seu nome de usuario?:")
senha = input("Digite sua senha:")

if (usuario == "admin" or usuario == "root") and senha == "12345":
    print("Acesso liberado")
else:
    print("Acesso negado")    