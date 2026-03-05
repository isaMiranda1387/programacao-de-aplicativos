print("--- OPERADOR PRENSA HIDRÁULICA ---")

curso = input("Concluiu o curso de segurança? (S/N):")

if curso == "S":
    print("Ok, proxima pergunta.")
    instrutor = input("O instrutor está presente na sala? (S/N):")
    if instrutor == "S":
        print("Acesso liberado: Operação iniciada.")
    else: 
        print("Aguarde o instrutor para ligar a máquina")   
else:
    print("Acesso Negado: Faça o treinamento primeiro")        