# -*- coding: utf-8 -*-

# Lista para colocar os inputs descrevendo as joias
jewels_list = []

# Loop para inserir os inputs na lista
while True:
    # Tratamento de erro usando End Of File Error para sair do loop
    try:
        jewels_list.append(input())
    except EOFError:
        break
# Transforamndo a lista em um set para que não exista itens duplicados
jewels_list = set(jewels_list)
# Imprimindo o tamanho set, que será o número de jóias únicas
print(len(jewels_list))
