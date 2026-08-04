from matriz_estocastica import matriz_estocastica

def matriz_google (grafo):
    coeficiente_google = 0.85
    matriz = matriz_estocastica(grafo)
    # print(matriz)
    matriz_unitaria = []
    n = len(matriz)
    #contruindo a matriz google
    for i in range(n):
        linha= []
        for j in range(n):
           linha.append((1- coeficiente_google)/n) # (1- coeficiente_google)/n que multiplica a matriz unitária nxn
        matriz_unitaria.append(linha)
  
    for i in range(n):
        for j in range(n):
            matriz[i][j]= matriz[i][j]*coeficiente_google #matriz de adjacencia * coeficiente_google

    for i in range(n):
        for j in range(n):
            matriz[i][j]= matriz[i][j] + matriz_unitaria[i][j]
    
    return matriz
    
 