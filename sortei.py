usuario = int(input("Qual o seu ID?"))
valor = float(input("Digite o seu valor?"))

if usuario % 2 == 0 and valor > 500.00:
    print(f"Parabéns usuário {usuario}! Você ganhou um cupom para sua compra de R${valor}")
else:
    print(f"Obrigado pela compra, usuário {usuario}. Continue acompanhando nossas promoções!")




