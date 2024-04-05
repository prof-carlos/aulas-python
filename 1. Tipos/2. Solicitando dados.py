import os

# Limpa o terminal.
os.system("cls || clear")

# Solicitando dados para o usuário.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

os.system("cls || clear")

# Exibindo dados inseridos pelo usuário.
print("\n=== Exibindo resultados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.3f}")


