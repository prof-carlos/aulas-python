import os
os.system("cls || clear")

quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0
quantidade_geral = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        
    soma_geral += numero
    quantidade_geral += 1

if quantidade_geral > 0:    
    media_pares = soma_pares / quantidade_pares
    media_geral = soma_geral / quantidade_geral

    print(f"\nQuantidade de pares: {quantidade_pares}")
    print(f"Quantidade de ímpares: {quantidade_impares}")
    print(f"Média de números pares: {media_pares}")
    print(f"Média geral: {media_geral}")
else: 
    print("\nNão foram informados números necessários para a operação.")

    
    