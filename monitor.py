temperatura = float(input("Qual a temperatura atual?:"))


if temperatura <= 30:
    print("Clima estável")
else:
    print("Alerta de calor!")    
 
    
    
umidade = float(input("Qual a umidade?:"))

if umidade < 40:
    print("Ação, ligar irrigação!")
else:
    print("Ação ligar apenas ventiladores")    

