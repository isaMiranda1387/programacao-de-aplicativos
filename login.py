senha = input("Qual a sua senha?: ")
tentativas = int(input("Qual o número de tentativas?: "))
token = input("Você possui TOKEN? (S/N): ")

if senha == "admin123" and (tentativas % 3 == 0 or token == "S"):
    print(f"Tentativa n°{tentativas}: ACESSO CONCEEDIDO")
else:
    print(f"Tentativa n°{tentativas}: ACESSO BLOQUEADO POR PROTOCOLO")    
