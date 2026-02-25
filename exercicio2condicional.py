poder = int(input("Qual seu poder de ataque?"))
defesa = int(input("Quantos pontos de defesa possuiu?"))

Resultado = poder - defesa  

if Resultado <= 0:
    print("O vilão bloqueou o ataque! Dano: 0")
if Resultado > 0:
    print("Ataque crítico! Você causou dano ao vilão de ", Resultado)    