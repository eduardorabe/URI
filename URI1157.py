# -*- coding: utf-8 -*-

while True:
    t = int(input())

    if t == 0:
        break

    matriz = list()

    # Faz o esqueleto da matriz e preenche com 0
    for x in range(t):
        matriz.append([])
        for y in range(t):
            matriz[x].append(0)

    # Preenche a matriz com os valores desejados
    for x in range(t):
        for y in range(t):
            matriz[x][y] = 2 ** (x + y)

    # Obtem o numero de digitos do maior numero da matriz e transforma a matriz de inteiros em uma matriz de strings
    # com o numero correto de digitos
    comprimento_minimo = len(str(matriz[t - 1][t - 1]))

    for x in range(t):
        for y in range(t):
            if len(str(matriz[x][y])) < comprimento_minimo:
                while len(str(matriz[x][y])) < comprimento_minimo:
                    matriz[x][y] = " " + str(matriz[x][y])
            else:
                matriz[x][y] = str(matriz[x][y])

    # Imprime a matriz com o espacamento desejaddo de um espaco entre as strings e uma linha apos a matriz
    for x in range(t):
        for y in range(t):
            if y < t - 1:
                print(matriz[x][y], end=" ")
            else:
                print(matriz[x][y], end="\n")
    print()
