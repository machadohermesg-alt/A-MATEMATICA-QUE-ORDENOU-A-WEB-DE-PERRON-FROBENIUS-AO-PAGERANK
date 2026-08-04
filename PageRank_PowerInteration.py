from matriz_google import matriz_google

#A ideia é convergir piG = pi, atraves de interações, procurando a estabilidade
def PowerInteration(grafo, epislon, max_interações):
    matriz = matriz_google(grafo)
    n = len(matriz)

    #criando vetor com prob iguais
    v=[]
    for m in range(n):
        v.append(1/n)

    #configurando o maximo de interações, caso a convergencia seja muito devagar
    for interação in range(max_interações):
        v_novo = [] #possivel candidato

        #Pecorrendo coluna, para analisar quantas paginas se conectam a pagina de cada coluna
        for j in range(n):
            soma=0
            #Somandos as saidas para cada i para este j
            for i in range(n):
                soma = soma + v[i] * matriz[i][j] 
            v_novo.append(soma)#adicionando no vetor novo

        diferenca =0 
        for l in range(n):
            diferenca = diferenca + abs(v[l]-v_novo[l])    
        v=v_novo
        if diferenca< epislon:
            break
    print(v)    
    return(v)
