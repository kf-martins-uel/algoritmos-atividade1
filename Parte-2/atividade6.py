# Atividade 6

salario = float(input("Digite o salário: "))

# Como o python é burro com float, se deixar salario*=1.x, ele sempre dá um valor aproximado. 
# Escrever como a = a + (a * 0.x) reduz um pouco esses problemas.
if salario < 800: 
   salario = salario + (salario*0.15)
elif salario <= 1500:
   salario = salario + (salario*0.1)
else:
   salario = salario + (salario*0.05)

print(f"Reajustado para: {salario}")