#BSF BUSCA EM LARGURA, ELE VISITA TODOS OS LINKS DE DO PRIMEIRO VETICES ANTES DE IR PROS OUTROS LOGO A ORDEM ESPERADA AQUI É
# A->B->C->E->D
def BFS(grafos_web,pagina_incial):
    visitados = [pagina_incial] # [] Para mostrar que queremos lista
    fila = [pagina_incial]
    while fila: #Equando lista nao tiver vazia faça:
        pagina_atual = fila.pop(0) #mostrando que o elemento que será retirado é o primeiro elemento da lista(fila)
        print("Acessei a página: ",pagina_atual)

        for link in grafos_web[pagina_atual]:
            if link not in visitados:
                visitados.append(link) #adicionando em visitados
                fila.append(link) #adicionando na fila e reciciando

#O codigo faz o seguinte, começamos por A, e adicionamos ele em visitados e fila
#Apos isso fazemos um while na fila, onde pagina_atual recebe o primeiro valor a ser retirado da fila A (agora)
#apos isso fazemos um for nos valores de A, no caso B,C,E com isso eles são adicionaods em visitados em fila
#While continua e começa com B, onde ele é colocaod como pagina atual e removido da fila, com isso é visitado apenas C, que ja está na fila, logo nao faz nada
#while cnitnua e com C, onde ele é colocaod na pagina atual e remocido da fila, com isso visitamos A,D , como A ja está na fila executa o for novamente indo para D que não está na fila, logo adicionamos D
#A fila está E,D, logo executa, com E removendo e o adicionanod como pagina atual, com isso pecorremos ele, onde possudi com D que ja está em visitaods logo n ocorre nada,
#Por ultimo o ultimo elemento da fila é retirado e o codiog termina