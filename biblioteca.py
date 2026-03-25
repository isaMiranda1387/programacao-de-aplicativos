disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
emprestados = []

emprestimo = input("Digite o livro que deseja: ")
if emprestimo in disponiveis:
    disponiveis.remove(emprestimo)
    emprestados.append(emprestimo)
    print("Emprestimo realizado com sucesso!")
else:
    print("Desculpe, esse livro não está no acesso.")
    
if len(disponiveis) >= 2:
    del disponiveis[0:2]
    print(f"Livros disponíveis: {disponiveis} ")   
    print(f"Livros emprestados: {emprestados} ")     