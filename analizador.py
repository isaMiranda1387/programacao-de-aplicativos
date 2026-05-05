def contar_caracteres(texto):
    return len(texto)

usuario = input("Digite um nome de usuário: ")

quantidade = contar_caracteres(usuario)

if quantidade < 5:
    print("Nome de usuário muito curto")
else:
    print("Nome aceito")