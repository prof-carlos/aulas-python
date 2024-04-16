import os

os.system("clear")

primeiraNota: float = -1
segundaNota: float = -1
terceiraNota: float = -1

while (primeiraNota < 0 or primeiraNota > 10) :
    primeiraNota = float(input("Digite a primeira nota: "))

while (segundaNota < 0 or segundaNota > 10) :
    segundaNota = float(input("Digite a segunda nota: "))
    
while (terceiraNota < 0 or terceiraNota > 10) :
    terceiraNota = float(input("Digite a segunda nota: "))

media  = (primeiraNota + segundaNota + terceiraNota) / 3

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    