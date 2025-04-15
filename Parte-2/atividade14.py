# Atividade 14

n = int(input("Número de lados: "))

if n == 3:
   print("Triângulo")
elif n == 4:
   print("Quadrado")
elif n == 5:
   print("Pentágono")
elif n < 3:
   print("Não é um polígono")
elif n > 5:
   print("Polígono não identificado")