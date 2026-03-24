vagas = ["Livre" , "Ocupado" , "Livre" , "Ocupado"]
escolha = int(input("Digite um número de 0 a 3: "))
if escolha % 2 == 0 and vagas[escolha] == "Livre":
    print(f"Vaga {escolha} autorizada para estacionar. ")

else:
    print(f"{escolha} indisponivel ou fora das regras. ")    