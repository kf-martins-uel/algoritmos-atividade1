# Atividade 13

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a+b+c != 180):
   print("Não é triângulo! Soma dos ângulos internos diferente de 180.")
elif (a < 180 and a > 90) or (b < 180 and b > 90) or (c < 180 and c > 90):
   print("Obtuso") 
elif a == 90 or b == 90 or c == 90:
   print("Reto")
elif a > 0 or b > 0 or c > 0:
   print("Agudo")
