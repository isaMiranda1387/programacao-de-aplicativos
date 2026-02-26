Nome = "admin" 
Codigo = int(input("Qual o seu código secreto?:"))

Nome_usuario = input("Qual seu nome de usuário?:")

if Nome == "admin" and Codigo == 999:  
    print("Acesso ao servidor liberado. Sistema online.")
else:
    print("Falha na autenticação. Alerta de segurança ligado!")

