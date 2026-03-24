pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
concluido = []
print(f"Arquivo antigo pendente {pendentes} concluído {concluido}")
pendentes.pop(0)
concluido.append("Relatorio.pdf")
print(f"Arquivo novo pendente {pendentes} concluído {concluido}")
