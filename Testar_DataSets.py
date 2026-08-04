def ler_dados(caminho_arquivo):
    grafo ={}

    with open (caminho_arquivo, 'r', encoding = 'utf-8', errors= 'ignore') as arquivo: 
        for linha in arquivo: #pecorrendo cada linha do arquivo
           
           if linha.strip() == '': #caso haja espaço faça nada
                continue
           partes = linha.split() #separando cada coluna
          
           if partes[0]== 'n': #caso seja n ( como eles aparecem primeiro) adicionamos a chaves sendo vazia, ou seja criamos todos os vertices sem aresta
               grafo[partes[1]] = []
           elif partes[0] == 'e': # caso seja e adicionamos criamos o grafo direcionado, ou seja criamos as arestas
                grafo[partes[1]].append(partes[2])


        return(grafo)






      
       