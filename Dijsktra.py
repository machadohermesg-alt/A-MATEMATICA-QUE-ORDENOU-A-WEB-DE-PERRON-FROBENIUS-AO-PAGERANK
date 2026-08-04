#Dijsktra andar por caminhos que contem pesos  
def Dijsktra (grafo,vertice_inicial, vertice_final):
    peso_acumulado = 0
    print("Começamos do vértice ", vertice_inicial)
    visitados=[vertice_inicial]
    pilha=[vertice_inicial]
    vertice_atual = vertice_inicial
    caminhos ={vertice_inicial: 0}
    print(caminhos) 
    lista = []
    while pilha:

        
        vertice_atual = pilha.pop(0)
        for vertices in grafo[vertice_atual]:  
                if vertices not in visitados:
                    visitados.append(vertices)
                    caminhos[vertices]= grafo[vertice_atual][vertices]
                    pilha.append(vertices)
                    print(caminhos)