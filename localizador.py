cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome = input("Digite o nome da cidade que deseja: ")
if nome in cidades:
    posicao = cidades.index(nome)
    print(f"A cidade {nome} está na posição {posicao}")
else:
    print(f"A cidade {nome} não foi encontrada na lista.")    