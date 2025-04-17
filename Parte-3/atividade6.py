# Atividade 6

for i in range(10):
   nome = input("Digite o nome: ") 
   idade = int(input("Digite a idade: "))
   sexo = input("Digite o sexo [M, F]: ")

   if sexo.lower() == 'm' and idade >= 21:
      print(nome)