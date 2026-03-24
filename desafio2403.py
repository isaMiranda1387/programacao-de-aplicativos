autorizados = ["Alice" , "Bob" , "Carlos"]
entrada_de_dados = input("Digite o nome do pesquisador:")
if entrada_de_dados in autorizados: 
    print(f"Acesso Permitido! O pesquisador {entrada_de_dados} está na posição" , autorizados.index(entrada_de_dados))
    pergunta = input("Deseja remover esse pesquisador da lista? (S/N):")
    if pergunta == "S":
        autorizados.remove(entrada_de_dados)
        print(f"Agora os membros da lista são {autorizados}")
    else:
       print("Encerrando o programa...")    
else:
   print(f"Acesso negado! O pesquisador {entrada_de_dados} não foi encontrado.")
   pergunta2 = input("Deseja cadastrar esse novo pesquisador (S/N)")
   if pergunta == "S":
      autorizados.append(entrada_de_dados)
      print(f"Lista autorizada {entrada_de_dados}")
   else:
       print("Encerrando o programa...")
      
      