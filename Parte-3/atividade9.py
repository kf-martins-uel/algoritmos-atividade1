# Atividade 9

n = int(input("Digite um número: "))
print(f"{'Número':<10}{'Fatorial':<13}")
for i in range(1, n+1):
    fat = 1
    for f in range(i):
        fat *= (f+1)
    print(f"{i:<10}{fat:<13}")