# Atividade 15

nota = float(input("Nota quantitava [0, 10]: "))

if nota < 2: 
   print("Sem rendimento")
elif nota < 4: 
   print("Mau")
elif nota < 6: 
   print("Regular")
elif nota < 8.5: 
   print("Bom")
else:
   print("Excelente")
