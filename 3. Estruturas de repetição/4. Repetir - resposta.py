import os

os.system("clear")

nota : float = -1
soma : float = 0
quantidadeNotas = 0

while True :
    nota = float(input("Digite a primeira nota: "))
    
    resposta = input("Deseja inserir mais uma nota: ")
    
    if  resposta == "sim":
        soma += nota
        quantidadeNotas += 1
    else:
        break

media  = soma / quantidadeNotas

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    
    
