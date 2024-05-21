import os
os.system("clear")

# Constante para 3 notas.
QUANTIDADE_NOTAS = 2

# Vetor.
notas = []

print("\nSolicitando dados para o usuário.")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / QUANTIDADE_NOTAS

print("\nExibindo resultados")
# ForEach.
for nota in notas:
    print(f"Nota: {nota}")

print(f"Média: {media}")
