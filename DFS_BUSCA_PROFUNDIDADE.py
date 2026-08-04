#DFS Busca em Profundidade -DEPTH-FIRST SEARCH RECURSIVO(RUIM PARA GRAFOS GRANDES)
#ORDEM ESPERADA NO NOSSO GRAFO:
#A ->B->C->D->E
def DFS_R(grafos_web, pagina_atual, visitados):
    visitados.append(pagina_atual) # adicionando como visitados a pagina atual
    print("Acessei a página: ", pagina_atual)

    #grafos_web olhamos para aonde a chave que pagina_atual está apontando
    for link in grafos_web[pagina_atual]: #Verifica se o "link" que é o vertice que o vertice da pagina Atual esta apontado
        if link not in visitados: # ja foi visitado caso sim, nao faz nada e vamos para o proximo vertice, caso n tenha ela sera a nova pagina incial
            DFS_R(grafos_web,link,visitados) #recursão pesado
            #Quando todos as paginas que tem link com pagina_atual foram visitados ele roda e para

            
#DFS INTERATIVO AGORA, RECURSIVO É BRUTAL, que muda a ordem devido o POP NO ULTIMO ELEMENTO
def DFS_I(grafos_web,pagina_inicial):
    visitados =[pagina_inicial]
    pilha= [pagina_inicial]
    
    while pilha:
        pagina_atual= pilha.pop() #Adicionando visitado no vertice retirarado que é o ultimo
        print("Acessei a página", pagina_atual)
        
        for link in reversed(grafos_web[pagina_atual]):
            if link not in visitados:
                visitados.append(link)
                pilha.append(link)