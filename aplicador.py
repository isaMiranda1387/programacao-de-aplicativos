def  aplicar_promocao(promocao):
    lista= [150.0 , 80.0 , 200.0 , 50.0]
    listas=[]
    for desconto in lista:
        if len(desconto) >= 100:
            return "Nova lista"

lista_com_desconto = float(input(f"A lista atual é {lista_com_desconto}"))
msg = aplicar_promocao(lista_com_desconto)
print(msg)
