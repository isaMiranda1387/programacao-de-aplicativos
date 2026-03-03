nome = (input("Digite seu nome:"))
valor_Total = float(input("Valor total da compra:"))
distancia = int(input("Qual a distância da em entrega em km:"))
cupom_Especial = input("Cupom especial:")

desconto = 0.0

if valor_Total >= 1000.0 and cupom_Especial == "S":
   desconto = Valor_Total * 0.20 
   
elif valor_Total >= 500 and cupom_Especial == "S":
    desconto  = valor_Total * 0.10

frete = 40.0

if distancia <= 50 and desconto > 200: 
    frete = 0.00
 
valor_Total = desconto + frete

if desconto == (valor_Total * 0.20):
    print("Parabéns, Você ganhou um Mousepad Gamer de brinde!")




