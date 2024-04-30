import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


# Função sem retorno.
def mostrarTabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para tabuada de multiplicação: "))

mostrarTabuada(numero)