def converter_km_par_ms(velocidade_kmh):
    return velocidade_kmh / 3.6

velocidade = float(input("Digite a velocidade em km/h: "))

if velocidade > 80: 
    velocidade_ms = converter_km_par_ms(velocidade)
    print(f"Velocidade em m/s: {velocidade_ms:}")
    print("Reduza a velocidade!")
else:
    print("Velocidade dentro do limite. ")    