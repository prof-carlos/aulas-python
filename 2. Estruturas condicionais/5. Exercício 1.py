import os

os.system("cls || clear")

nome: str
idade: int
primeiraNota : float
segundaNota : float
terceiraNota : float
quartaNota : float
soma: float
media: float

nome = input("Digite seu nome: ")
idade = input("Digite a idade: ")
primeiraNota = float(input("Digite a primeira nota:"))
segundaNota = float(input("Digite a segunda nota:"))
terceiraNota = float(input("Digite a terceira nota:"))
quartaNota = float(input("Digite a quarta nota:"))

# soma = primeiraNota + segundaNota + terceiraNota + quartaNota
# media = soma / 4

media = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

print("\n=== Exibindo resultados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Terceira nota: {terceiraNota}")
print(f"Quarta nota: {quartaNota}")
print(f"Média: {media}")

print("=== Fim ===")
