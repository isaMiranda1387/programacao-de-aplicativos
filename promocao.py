compra = float(input("Qaul o valor da compra?:"))
cliente = input("Você é Prime? (S/N):")
frete = 50.00

if compra >= 500.00 or (cliente == "S" and compra >= 100.00):
    print("Parabens voce ganhou frete gratis!")
    frete = 0.0 
    print("valor_total" , compra)

valor_total = compra + frete 
print("valor total" , valor_total)    




