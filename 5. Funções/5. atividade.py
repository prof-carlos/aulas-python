import os
os.system("cls || clear")

def verificar(numero):
    if numero > 0:
        print("O número é positivo.")
    elif numero == 0:
        print("O número zero é neutro.")
    else:
        print("O número é negativo.")


print("Verificando se um número é positivo ou negativo.")
numero = int(input("Digite um número: "))
verificar(numero)

    