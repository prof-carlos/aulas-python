import os

os.system("clear")

nota : float = -1
soma : float = 0

QUANTIDADE_DE_NOTAS = 3

for i in range(QUANTIDADE_DE_NOTAS):
    while True :
        nota = float(input("Digite a primeira nota: "))
        if  nota < 0 or nota > 10:
            print("Nota inválida... \n")
        else: 
            soma += nota
            break

media  = soma / QUANTIDADE_DE_NOTAS

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    
    
