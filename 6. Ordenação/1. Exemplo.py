import os

os.system("cls || clear")

def ordenacaoPorSelecao(lista):
    tamanhoDaLista = len(lista)

    for j in range(tamanhoDaLista - 1):
        indiceMenorNumero = j
        for i in range(j, tamanhoDaLista):
            if lista[i] < lista[indiceMenorNumero]:
                indiceMenorNumero = i
        if lista[j] > lista[indiceMenorNumero]:
            aux = lista[j]
            lista[j] = lista[indiceMenorNumero]
            lista[indiceMenorNumero] = aux

lista = [8, 6, 4, 2]

# Mostrando lista desordenada.
print(f"Lista desordenada: {lista}")

# Ordendando lista.
ordenacaoPorSelecao(lista)

# Mostrando lista ordenada.
print(f"Lista ordenada: {lista}")