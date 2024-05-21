import os

os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

alunos = []

dicinario = {}

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    aluno = {"nome" : nome, "idade" : idade}
    alunos.append(aluno)

for i in alunos:
    print(f"Nome: {i['nome']}")
    print(f"Idade: {i['idade']}")