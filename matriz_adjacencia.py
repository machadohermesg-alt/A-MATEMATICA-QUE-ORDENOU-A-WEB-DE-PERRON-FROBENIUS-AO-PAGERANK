def matriz_adjacencia(grafo):
    vertices = sorted(grafo.keys()) #Arruma em ordem alfabetica os elementos
    n = len(grafo) #Determina a largura e altura da matrz quadrada (n*n)
    matriz = []

    for i in range(n): #Cria uma matriz com todos elementos zerados
        linha = []
        for j in range(n):
            linha.append(0.00)
        matriz.append(linha)    
    
    for origem in grafo: #pecorre a chaves primarias do dicionario
        i = vertices.index(origem) #pega qual posição está tipo o primeiro elemento de origem no grafo é a posição 0 da lista referente a A
        for destino in grafo[origem]: #pecorre os valores do diconario
            j = vertices.index(destino)#pega qual elemento está em primeiro relacionado com a letra A que no caso é B que recebera 1, pois A->B
            matriz[i][j]= matriz[i][j] +1
    # for linha in matriz:
    #     print(linha)
    return(matriz)

