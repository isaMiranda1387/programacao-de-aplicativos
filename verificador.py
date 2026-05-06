def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False   
    
usuario = int(input("Digite um número: ")) 

if eh_par(usuario):
    print("Este número é par! ")
else:
    print("Este número é ímpar! ")    
