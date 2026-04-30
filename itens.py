def esta_na_lista(lista_nomes, nome_buscar):
    for item in lista_nomes:
        if item == nome_buscar:
            return "Encontrado!"
    return "Não disponível"


frutas = ["Abacaxi", "Banana", "Melancia", "Amora", "Morango"]

print(esta_na_lista(frutas, "Banana"))
print(esta_na_lista(frutas, "Manga"))
