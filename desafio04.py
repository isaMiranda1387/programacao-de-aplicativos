print("---- SISTEMA DE POUSO DE DRONES DE CARGA ----")

codigo = int(input("Qual o código do drone:"))
autorizacao = input("Você possuiu autorização da torre? (S/N):")

if codigo == 999 or autorizacao == "S":
    print("Drone identificado.")
    
    bateria = int(input("Qual o nível de bateria do drone?:"))
    clima = input("O clima está ensolarado ou chuvoso?:")
    vento = int(input("Qual a velocidade do vento?:"))
    
    if bateria < 10:
        print("Pouso AUTORIZADO IMEDIATAMENTE por segurança.")
    elif bateria >= 10:
        if (clima == "ensolarado" and vento < 30) or (clima == "chuvoso" and vento < 10):
            print("POUSO AUTORIZADO!")
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")             
else:
    print("Drone não identificado. Retornando à base.")   

