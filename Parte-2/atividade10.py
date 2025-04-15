# Atividade 10

idade = int(input("Idade: "))
sexo = input("Sexo [M/F]: ")

if sexo.lower() == "m" and idade >= 65:
   print("Pode se aposentar")
elif idade >= 60:
   print("Pode se aposentar")
else:
   print("Não pode se aposentar")