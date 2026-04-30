def sofrer_dano(valor_dano):
    vida -= valor_dano
    return vida

vida = 100
while vida > 0:
    print(f"Vida atual: {vida}")
    
    dano = int(input("Digite o dano causado pelo monstro: "))
    vida = sofrer_dano(vida,dano)

print("Game Over")    