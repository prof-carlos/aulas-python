import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== ===== === ")
    print("=== SENAI === ")
    print("=== ===== === ")

# Solicitando dados para o usuário.    
logoSenai()
nome = input("Digite seu nome: ")

logoSenai()
idade = int(input("Digite sua idade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

# Exibindo dados para o usuário.
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")


