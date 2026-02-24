produto = (input("nome do produto:"))
preco = float(input("preço do produto:"))
quantidade = int(input("quantidade do produto:"))

multiplicacao = preco * quantidade


print("a soma dos valores é:", multiplicacao)


print("Recibo:")
print("Nome do produto:", produto)
print("Quantidade:", quantidade)
print("Total a ser pago:", multiplicacao)