lista = [1, 5, 8, 12, 15, 22, 7, 9, 30, 4]
pares = []
impares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista de números: ", lista)    
print("Lista de números: ", pares)
print("Lista de número: ", impares)
