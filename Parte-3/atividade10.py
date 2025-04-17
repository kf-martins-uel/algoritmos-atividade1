# Atividade 10

# Soma de PA - s = (a1 +a2)*n/2
# (201-25)/2 = n
# soma = (25+201)*n/2
soma = 0
for i in range(26, 202, 2):
    soma += i
print(soma)