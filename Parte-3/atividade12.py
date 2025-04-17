# Atividade 12

print(f"{'Fahrenheit':<12}{'Celsius':<15}")
f = 50
while f<=150:
    c = ((f-32)*5)/9
    print(f"{f:.<12}{c:.2f}")
    f+=1
