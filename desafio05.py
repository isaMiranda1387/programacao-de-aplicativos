quantidade = int(input("Qual o número total de garrafas que já passaram pela esteira hoje?:"))

if quantidade == 500:
    print("HORA DA LIMPEZA: pare a máquina imediatamente!")   
    print("QUALIDADE: retire a amostra para teste!") 

elif quantidade % 500 == 0:
    print("HORA DA LIMPEZA: pare a máquina imediatamente!")

elif quantidade % 100 == 0:
    print("QUALIDADE: retire a amostra para teste!")    

else:
    print(f"Produção em dia. Garrafa número {quantidade} processada.")  