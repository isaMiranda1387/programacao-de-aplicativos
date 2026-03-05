print("---- INSPETOR DE QUALIDADE ----")

comprimento = input("O comprimento da peça está entre 10cm e 12cm (S/N)") 

if comprimento == "S":

    largura = input("A largura da peça está entre 5cm e 6cm? (S/N)")
    if largura == "S":
        print("Peça aprovada!")
    else:
        print("Reprovado, peça inválida")    
else:
    print("Reprovado, peça inválida")
                 
   



