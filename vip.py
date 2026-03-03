idade = int(input("Insira sua idade:"))
ingresso = input("Possui ingresso? (S/N):")
lista = input("Possui nome na lista? (S/N)")

if (idade >= 18 and ingresso == "S") or lista == "S": 
    print("Seja bem vindo")
else:
    print("Acesso negado.")    