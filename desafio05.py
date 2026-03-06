quantidade = int(input("Qual o número total de garrafas que já passaram pela esteira hoje?:"))

if garrafas % 500 == 0:
    print("HORA DA LIMPEZA: pare a máquina imediatamente!")

if garrafa % 100 == 0:
    print("QUALIDADE: retire a amostra para teste!")    