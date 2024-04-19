notas = []

while True:
  nota = float(input("Digite a nota do aluno: "))
  notas.append(nota)

  continuar = input("Deseja digitar outra nota? (s/n): ")
  if continuar.lower() != "s":
    break

for i in range(len(notas)):
    print(f"{i+1}ª nota: {notas[i]}")
