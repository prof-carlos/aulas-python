import os

os.system("clear")

soma : float = 0
quantidadeNotas = 0

while True :
    nota = float(input("Digite a primeira nota: "))
    
    resposta = input("Deseja inserir mais uma nota: ")
    resposta = resposta.upper()

    soma += nota
    quantidadeNotas += 1
    
    if  resposta == "N":
        break

media  = soma / quantidadeNotas

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    
    
