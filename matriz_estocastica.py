from matriz_adjacencia import matriz_adjacencia
#Basicamente essa matriz irá utilizar a probalidade por exemplo A se conecta com B,C, D, mas B possui 2 links vindo de A, o restante é 1, logo temos 2+1+1
# entaõ a pprob de ir para B é 2/4 = 50% isso é a matriz estocástica(Matriz de transição) ONDE A SOMA DAS LINHA SEMPRE É 1(ANALISAR), explicação caso uma
#pessoa entra numa pagia que não possui links, conseguir retornar e outra para outros na barra de pesquisa.
def matriz_estocastica (grafo):
    matriz= matriz_adjacencia(grafo) 
    soma_prob = 0
    lista_soma_prob = []
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            soma_prob = soma_prob + matriz[i][j]
        lista_soma_prob.append(soma_prob)
        soma_prob = 0
    # print(lista_soma_prob)
    for i in range(n):
        for j in range(n):
            if lista_soma_prob[i] != 0:
                matriz[i][j] = matriz[i][j]/lista_soma_prob[i]
            else:
                matriz[i][j] =1/n 
    # for linha in matriz:
    #     print(linha)
    return(matriz)    