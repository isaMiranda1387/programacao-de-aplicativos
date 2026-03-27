compras = []
item = ""
while item != "fim":
    item = input("Item a ser adicionado na lista: ")
    compras.append(item)
compras.remove("fim")
print(f"Fim da lista de compras, a lista atual agora é: {compras}")