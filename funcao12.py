def analisar_vendas(nome, lista_vendas, meta_mensal):
    total = 0
    for item in lista_vendas:
        total += item 

    media = total/len(lista_vendas)

    if media >= meta_mensal:
        rpmt = ("bateu")
    else:
        rpmt = ("não bateu")

    return f"O vendedor {nome} teve média de {media} e {rpmt} a meta"

usuario = input("Digite seu nome: ")
lista =  [1200.00, 1500.00, 1100.00, 1900.00]
meta = float(input("Digite sua meta: "))

chamada = analisar_vendas(usuario, lista, meta)
print(chamada)    
