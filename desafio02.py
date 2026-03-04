cargo = input("digite seu cargo:")
codigo = int(input("digite seu codigo de acesso:"))
botao = input("o botão de emergencia esta precionado? (S/N)")
epi = input("voce esta utilizando o epi completo? (S/N)")

if cargo == "engenheiro" or "tecnico" and (codigo == 1234 or botao == "S"):
    print("acesso liberado")

else:
    print("acesso negado!")    