temperatura = float(input("digite a temperatura atual:"))

if temperatura >= 80:
    print("PERIGO! Desligando servidor por superaquecimento!")
elif temperatura >= 50: 
    print("Alerta: Ventoinhas ligadas no máximo!")
elif temperatura < 50:
    print("Temperatura estável. Sistema operando normalmente")    
