# Atividade 14

n = hc = mi = m = 0
for i in range(15):
    nome = input("Digite o nome: ")
    altura = float(input("Digite a alura: "))
    sexo = input("Digite o sexo [m,f]: ")
    olhos = input("Digite a cor dos olhos (c - castanhos; a - azuis; v - verdes): ")
    if sexo.lower() == 'm' and olhos.lower() == 'c':
        hc+=1
    elif sexo.lower() == 'f':
        m+=1
        mi += 1 if altura<1.6 else 0
print(f"Total de homens com olhos castanhos: {hc}\nTotal de mulheres: {m}\nTotal de mulheres com altura menor que 1.60m: {mi}")