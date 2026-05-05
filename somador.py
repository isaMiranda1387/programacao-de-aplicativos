def somar_carrinho(precos , total):
    for p in precos:
        total += p 

    if total > 500:
        desconto = total * 0.10
        total_final = total - desconto
        return total_final
    return total     

lista_compras = [120.50, 89.90, 300.00, 45.60]
total = 0 
valor_final = somar_carrinho(lista_compras, total)
print(f"Valor final a pagar: R$ {valor_final:}")
