import json

frase = input("Digite uma frase: ")

dados = {
    "mensagem": "Sua frase aqui "
}

with open("teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

print("Arquivo salvo com sucesso!")



