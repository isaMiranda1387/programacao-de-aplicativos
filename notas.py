def avaliar_desenpenho(nota):
    if nota >= 9: 
        return "Execelente"
    elif nota >= 7:
        return "Bom"
    elif nota > 5:
        return "Regular"
    else:
        return "Insuficiente"
    
nota_usuario = int(input("Digite sua nota: "))

mensagem = avaliar_desenpenho(nota_usuario)   
print(mensagem) 