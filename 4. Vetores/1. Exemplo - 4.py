import os

os.system("clear")

notas = []

for i in range(300):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)



# ForEach.
for i in notas:
    print(f"Nota: {i}")
