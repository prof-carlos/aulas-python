"""
Escreva um algoritmo que leia a nota de um aluno. 
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.

Mostre a nota informada pelo usuário.
"""

import os

os.system("clear")

nota: float = -1

while (nota < 0 or nota > 10) :
    nota = float(input("Digite uma nota: "))

print(f"Nota informada: {nota}")

print("=== Fim === ")