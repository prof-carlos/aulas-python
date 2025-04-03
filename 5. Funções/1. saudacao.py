import os
os.system("cls || clear") 

# Função sem retorno.
# Definindo características da função.
def saudacao(nome, sobrenome):
    print(f"Olá {nome} - {sobrenome}! Bem-vindo(a) ao curso de DS!")

# Crie uma função com o nome: disciplina(nome) que receba o nome de 
# uma disciplina do curso de DS. 
# Mostre o texto: A disciplina *** faz parte do curso de DS.
def disciplina(nome):
    print(f"A disciplina {nome} faz parte do curso de DS.")
    
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_disciplina = input("Digite o nome da disciplina: ")
    
saudacao(nome, sobrenome) # Chamando a função.
disciplina(nome_disciplina) # Chamando a função.