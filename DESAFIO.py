print("Preencha os dados a seguir:")

Nome = str(input("Digite seu nome:"))
Valor_Total = float(input("Valor total da compra:"))
Distancia = int(input("Qual a distância da em entrega em km:"))
Cupom_Especial = input("Cupom especial:")
Frete = 40.00

if Valor_Total >= 1000 and Cupom_Especial == "S":
   Desconto_Vip = Valor_Total * 0.20 
   Valor_com_desconto = Valor_Total - Desconto_Vip 
   print("Parabéns! Você ganhou um Mouse pad Gamer de brinde!")
elif Valor_Total >= 500 and Cupom_Especial == "S":
   Desconto_Padrao = Valor_Total * 0.10
   Valor_com_desconto = Valor_Total - Desconto_Padrao
   print("Parabéns, você ganhou 10% de desconto! Seu valor agora é:", Valor_com_desconto)

elif Distancia <= 50 and Valor_com_desconto > 200: 
    frete = 0.00
    total = Valor_final + frete 
else:
    total = Valor_final + frete 

print("Nome:", Nome)    
print("Valor Total:", Valor_Total)
print("Cupom especial:", Cupom_Especial)
print("Valor final a pagar:", total)





