import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Função com retorno.
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

# Solicitando dados para o usuário.    
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)

# Exibindo dados para o usuário.
print(f"Soma: {soma}")



