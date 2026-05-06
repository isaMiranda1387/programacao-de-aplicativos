def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    valorimp = valor_base + imposto_percentual
  
    if cupom_desconto > valorimp: 
        precof = 0
        return precof 
    elif cupom_desconto > 0:
        precof = valorimp - cupom_desconto
        return precof 
    return valorimp 

valor_base = int(input("Dgite o valor do produto: "))
imposto_percentual = int(input("Digite o valor do imposto: "))
cupom_desconto = int(input("Digite o valor do desconto: "))

chamada = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)
print(chamada)