lista = ["Isadora", "João", "Arthur", "Alice", "Maria"]
while lista[0] != "Maria":
    lista.pop(0)
    print("Lista: ", lista)
if lista[0] == "Maria":
    print("Maria atendida.")