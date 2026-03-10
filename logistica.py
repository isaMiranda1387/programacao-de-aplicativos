codigo = int(input("Qual o código do pacote? "))
peso = float(input("Qual o peso do pacote? "))


if peso < 5 and (codigo % 10 == 0):
    print(f"Pacote {codigo}: ENTREGA EXPRESSA")
elif peso > 50 :
    print(f"Pacote {codigo}: CARGA PESADA")    