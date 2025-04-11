# Atividade 8

altura = float(input("Altura: "))
sexo = input("Sexo [m, f]: ")
pesoIdeal = 0

if sexo == 'm':
   pesoIdeal = (72.7*altura)-58
else:
   pesoIdeal = (62.1*altura)-44.7

print(f"Peso ideal: {pesoIdeal: 0.2f}")