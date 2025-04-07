# Atividade 2

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media  = (nota1 + nota2) / 2

print(f"Média: {media:.2f}")

if media >= 7.0:
   print("Aprovado por Média")
else:
   print("Não aprovado por Média")