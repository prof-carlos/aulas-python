import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float

# Nome do arquivo
arquivoDeOrigem = 'Dados_pessoais.txt'

# Lista para armazenar os alunos lidos
listaAlunos = []

# Lê os dados do arquivo
with open(arquivoDeOrigem, 'r') as arquivo:
    for linha in arquivo:
        nome, idade, peso, altura = linha.strip().split(',')
        listaAlunos.append(Aluno(nome=nome, idade=int(idade), peso=float(peso), altura=float(altura)))

# Exibe os dados lidos
print("\nExibindo dados.")
for aluno in listaAlunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")
    print(" === ")