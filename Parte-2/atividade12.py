# Atividade 12

x = int(input("x: "))
y = int(input("y: "))

if x == 0 or y == 0:
   print("Nenhum quadrante")
elif x > 0 and y > 0:
   print("Está no primeiro quadrante")
elif x < 0 and y > 0:
   print("Está no segundo quadrante")
elif x < 0 and y < 0:
   print("Está no terceiro quadrante")
elif x > 0 and y < 0:
   print("Está no quarto quadrante")