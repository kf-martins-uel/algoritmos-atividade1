# Atividade 5

valor = float(input("Diigte o valor: "))
taxa = float(input("Diigte a taxa (em %): "))
tempo = float(input("Diigte o tempo (dias): "))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"A prestação será {prestacao:.2f} unidades de dinheiro")
