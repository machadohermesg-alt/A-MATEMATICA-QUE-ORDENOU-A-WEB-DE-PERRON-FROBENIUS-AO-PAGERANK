from Grafos import grafos_web1,grafos_web2, grafo_pesado, grafos_web3, grafos_web4,grafos_web5,grafos_web6,grafos_web7,grafos_web8,grafos_web9,grafos_web10,grafos_web11
from DFS_BUSCA_PROFUNDIDADE import DFS_R, DFS_I

from BFS_BUSCA_LARGURA import BFS

from Dijsktra import Dijsktra

from matriz_adjacencia import matriz_adjacencia

from matriz_estocastica import matriz_estocastica

from matriz_google import matriz_google

from PageRank import PageRank

import networkx as nx

from PageRank_PowerInteration import PowerInteration

from Testar_DataSets import ler_dados



# print("="*80)
# print("INICIO MATRIZ DE ADJACENCIA")
# matriz_adjacencia(grafos_web3)
# print("FIM MATRIZ DE ADJACENCIA")
# print("=-"*40)


# print("="*80)
# print("INICIO MATRIZ ESTOCÁSTICA")
# matriz_estocastica(grafos_web3)
# print("FIM MATRIZ ESTOCÁSTICA")
# print("=-"*40)


# matriz_googlev=matriz_google(grafos_web3)
# for linha in matriz_googlev:
#     print(linha)


#biblioteca pagerank
def pageRankBli(grafo):
    G = nx.DiGraph()
    
  
   
    G.add_nodes_from(grafo.keys())
   

    for origem in grafo:
        for destino in grafo[origem]:
            if G.has_edge(origem,destino):
                G[origem][destino]['peso'] +=1
            else:
                G.add_edge(origem,destino, peso=1)    
                
    resultado = nx.pagerank(G, alpha=0.85, weight='peso')
    print(resultado)




 
#utilizando todos os grafos criados no projeto   
# cont = 1    
# grafos_lista = [grafos_web1,grafos_web2, grafos_web3, grafos_web4,grafos_web5,grafos_web6,grafos_web7,grafos_web8,grafos_web9,grafos_web10]
# for grafos in grafos_lista:

#     print("=="*40)
#     print("Interação no grafo: ",cont," ",grafos)
#     pageRankBli(grafos)
#     PageRank(grafos)
#     PowerInteration(grafos, 0.00001,10000)
#     print("=="*40)
#     print(' '*40)
#     cont=cont+1

         
#utiliza o dataset
#contando arestas e vertices
total_aresta = 0
grafo = ler_dados('gr0.epa.txt') #escolhendo o grafo
for origem in grafo:
    total_aresta = total_aresta + len(grafo[origem]) #olha quantos valores há para aquela chave, ou seja quantas arestas e soma com o total anterior
#contando verticess
total_vertices = len(grafo)
    
    
import time

inicio = time.perf_counter()
#PowerInteration(ler_dados('gr0.epa.txt'),0.001,1000) #58.2 segundos 4772 vertices e 8965 arestas
pageRankBli(ler_dados('gr0.epa.txt')) #0.28 s
#resolver_sistema_numpy(ler_dados('gr0.epa.txt'))
#PageRank(ler_dados('gr0.epa.txt')) demorou muito e parei

#teste com com 1600 vertices e 769 arestas
#PowerInteration(ler_dados('teste.txt'),0.001,1000) #1.61 segundos
#PageRank(ler_dados('teste.txt')) #100.64 segundos
#resolver_sistema_numpy(ler_dados('gr0.epa.txt')) #18.30 segundos (errado parece)
#pageRankBli(ler_dados('teste.txt'))
fim = time.perf_counter()
print()
tempo_total = fim - inicio
print(f"O algoritmo rodou em {tempo_total:.6f} segundos. O grafo possui {total_vertices} vertices e {total_aresta} arestas")


