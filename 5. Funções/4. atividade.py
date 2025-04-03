import os
os.system("cls || clear")

def verificar(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é impar.")


print("Verificando se um número é par ou impar.")
numero = int(input("Digite um número: "))
verificar(numero)

    