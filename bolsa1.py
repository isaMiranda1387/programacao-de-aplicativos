media = float(input("Insira sua média:"))
renda = int(input("Insira sua renda:"))
publica = input("Veio de escola pública? (S/N)")

if media > 8.0 and (renda < 2000.00 or publica == "S"):
    print("Ganhou bolsa")
else:
    print("Não atende os requisitos")    