Valor_Total = float(input("Qual o valor total da compra?:"))
Cupom = input("Digite o código do cupom:")
 

if Cupom == "DEV10": 
    Desconto = Valor_Total * 0.10
    ValorD = Valor_Total - Desconto
    print("Valor com desconto:", ValorD)
else:
    print("Cupom inválido, tente novamente.")    