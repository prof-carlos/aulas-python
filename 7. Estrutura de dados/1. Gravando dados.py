import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_ALUNOS = 2

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "), 
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    alunos.append(aluno)

# Definindo arquivo para salvar os dados 
# inseridos pelo usuário.
arquivo = "Dados_pessoais.txt"

# Percorrendo o vetor e salvando os dados por linha.
with open(arquivo, "w") as arquivoDeAlunos:
    for aluno in alunos: 
        arquivoDeAlunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.peso}, {aluno.altura}\n")

# Confirmando que os dados foram salvos.
print("Dados salvos com sucesso.")
