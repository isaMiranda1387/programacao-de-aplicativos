def aplicar_promocao(lista_de_preco , nova_lista):
    for item in lista_de_preco:
        if item >= 100.0:
            desconto = item * 0.15
            valorat = item - desconto
            nova_lista.append(valorat)
        else:
            nova_lista.append(item)
    return nova_lista


lista = [150.0, 80.0, 200.0, 50.0]
listavz = []
msg = aplicar_promocao(lista , listavz)
print(msg)
