import json


with open("notas.json", "r", encoding="utf-8") as arquivo:
    notas = json.read(arquivo)

soma = notas["matematica"] + notas["portugues"]

print("Soma das notas:", soma)