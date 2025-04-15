# Atividade 11

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = b**2-4*a*c
print(f"delta: {d}")

if d < 0:
   print("Não possui raizes reais. ")
else:
   x1 = (-b + d**(1/2))/(2*a)
   x2 = (-b - d**(1/2))/(2*a)

   print(f"x1: {x1}\tx2: {x2}")