from matriz_google import matriz_google

def PageRank (grafo):
    matriz = matriz_google(grafo)
    n = len(matriz)
    matriz_transposta = []
    #criando a matriz nova zerada
    for i in range(n):
        linha = []
        for j in range(n):
           linha.append(0)
        matriz_transposta.append(linha)
    #coloando os termos transposto da matriz google       
    for i in range(n):
        for j in range(n):
            matriz_transposta[i][j]= matriz[j][i]  
    
    #criando a identidade
    matriz_identidade = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz_identidade.append(linha)
    for i in range(n):
        for j in range(n):
            if i == j:
                matriz_identidade[i][j]=1                       
    # G^T-I
    for i in range(n):
        for j in range(n):
            matriz[i][j] = matriz_transposta[i][j]- matriz_identidade[i][j]
    # print("=="*40)
    # for linha in matriz:
    #     print(linha)                 

#Utilizaremos uma propriedade, Seja v o autovetor temos (G^t-I)v=0 como vale perron temos tb pelo nucleo imagem dimNu(G^t)=1, com isso escolhemos 
#uma linha arbritaria onde todos os termos serão substituidos por 1, ficando v1+v2+...+=1 transformando o sistema com unica solução e ja o normalizando
    sistema=[]
    #irei escolhe o primeiro elemento
    for i in range(n):
        linha = []
        if i==0:
            for j in range(n+1):
                linha.append(1)
        else:
            for j in range(n+1):
                if j<n:
                    linha.append(matriz[i][j])
                else:
                    linha.append(0)
        sistema.append(linha)    


    # for linha in sistema:
    #     print(linha)
    # print("=="*40)    
    #resolvendo o sistema
    matriz_nova = []
    k=0 #em programação em geral começamos do 0
    #O Algortimo se trata de triangulização em primeira instancia, realizando a troca de linhas caso o pivô seja 0
    while k<=n-1: #K determina qual coluna queremos zerar, pois o indice começa de 0, logo 0,1,2..n-1 são n interações(n é quantidade de linhas)
        # print("valor de k ",k)
        if sistema[k][k] == 0: #verificando se o pivô é 0
            maior_valor =0 #instancionado o maior valor
            indice_maior_valor =0 #instancinado o indice do maior valor
            for m in range(k,n): # k mostra a interação, se ja escalonamos uma coluna precisamos, ir para a proxima, realizando passsagem de linha
                if abs(sistema[m][k]) > abs(maior_valor): #utilizando o maior valor absoluto, facilitando calculo da maquina
                    maior_valor = sistema[m][k]
                    indice_maior_valor= m
            sistema[k], sistema[indice_maior_valor] = sistema[indice_maior_valor], sistema[k] #realizando a troca de linhas 
        pivo= sistema[k][k]   
        for i in range(k+1,n): #realizando as operações nas linhas posteriores ao pivô
            #if i>k: joguei no for
                # print(pivo)
                elemento = sistema[i][k] #elemento que será zerado
                coefic= elemento/pivo #o fator multiplicativo para zerar o elemento
                for j in range(k,n+1):#realizando a soma em todas as colunas posteriores, começando de k pois anterior ja foi realizado(otimização) e n+1 pois a matriz aumentada
                    # print(sistema[i][j])
                    #if j>=k: joguei no for
                        sistema[i][j]= -sistema[k][j]*coefic+ sistema[i][j] #realizando a substração, e conseguindo a triangulização
                        # print(" i = ", i, " j = ",j ," ", sistema[i][j])
        k=k+1            
    # for linha in sistema:
    #     print(linha)
    # print("=="*40)    

    #Resolvendo o sistema, como possui solução não há necessidade de preoucupar com divisão por 9=0
    k=0
    auto_vetor = []
    for i in reversed(range(n-k)):
        
        valor = sistema[n-1-k][n]/sistema[n-1-k][n-1-k]  
        auto_vetor.insert(0,valor)        
        # print(auto_vetor)
        for h in range(n-k-1):
            
            sistema[h][n-1-k]= valor*sistema[h][n-1-k]
            sistema[h][n]= sistema[h][n]-sistema[h][n-1-k]
           
        k=+k+1  
    print(auto_vetor)
    return(auto_vetor)   
        