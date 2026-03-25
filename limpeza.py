usuarios = ["admin", "convidado", "suporte", "teste"]
print(f"Lista antiga: {usuarios}")
usuarios.remove("teste")
del usuarios[0]
print(f"A lista atual: {usuarios}")