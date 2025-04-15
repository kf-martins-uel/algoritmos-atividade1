# Atividade 9

idade = int(input("Digite a idade: "))

if idade < 5 or idade > 60:
   print("Inválida")
elif idade <= 7:
   print("Infantil A")
elif idade <= 10:
   print("Infantil B")
elif idade <= 13:
   print("Juvenil A")
elif idade <= 10:
   print("Juvenil B")
else: 
   print("Sênior")
