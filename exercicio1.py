Nome = (input("Insira seu nome:"))

altura = float(input("Insira sua altura"))

if altura < 1.50:
    print("Desculpe, você não tem altura mínima", Nome)
elif altura >= 1.50:
    print("Acesso liberado! Divarta-se na queda livre", Nome)    