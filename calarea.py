def calcular_area(largura, comprimento):
    return largura * comprimento 

contador = 0

while contador < 3:
    print(f"Terreno {contador + 1}")
    
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    
    area = calcular_area(largura, comprimento)
    
    print(f"A área do terreno é: {area}")
    
    contador += 1