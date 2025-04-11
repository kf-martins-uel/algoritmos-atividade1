# Atividade 5

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
op = input("Digite um operador [+, -, *, /]: ")

if op == "+":
   print(n1+n2)
elif op == "-":
   print(n1-n2)
elif op == "*":
   print(n1*n2)
elif op == "/":
   print(n1/n2)
else:
   print("Operador inválido")