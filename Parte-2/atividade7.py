# Atividade 7

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1+n2)  / 2
print(f"Média: {media}")

if media <= 3:
   print("Reprovado sem rendimento")
elif media <= 6:
   print("Reprovado com Insuficiente")
elif media <= 7:
      print("Aprovado com Regular")
elif media <= 9:
      print("Aprovado com Bom")
elif media <= 10:
      print("Aprovado com Excelente")

