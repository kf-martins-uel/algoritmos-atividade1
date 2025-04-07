# Atividade 4

n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

if n1 == n2:
   print("São iguais")
else:
   print("Sao diferentes")
   if n1 > n2:
      print(f"{n2}, {n1}")
   else:
      print(f"{n1}, {n2}")