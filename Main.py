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
# print("INÍCIO do Algoritimo DFS, BUSCA EM PROFUNDIDADE RECURSIVO")
# DFS_R(grafos_web3,'A',[]) #1 Começa de A, Vai até B como B se conecta Com C vai até C, dps em C analisa se A ja foi visitado oq é afirmativo, indo para o proximo que é D QUE SE CONECTA COM E E GG
# print("=-"*40)
# print("FIM do Algoritimo DFS, BUSCA EM PROFUNDIDADE")

# print("="*80)
# print("INÍCIO do Algoritimo DFS, BUSCA EM PROFUNDIDADE INTERATIVO")
# DFS_I(grafos_web3,'A') #1 Começa de A, Vai até B como B se conecta Com C vai até C, dps em C analisa se A ja foi visitado oq é afirmativo, indo para o proximo que é D QUE SE CONECTA COM E E GG
# print("=-"*40)
# print("FIM do Algoritimo DFS, BUSCA EM PROFUNDIDADE")

# print("="*80)
# print("INÍCIO do Algoritimo BFS, BUSCA EM LARGURA")
# BFS(grafos_web3,'A') 
# print("=-"*40)
# print("FIM do Algoritimo BFS, BUSCA EM LARGURA")

# #Dijsktra(grafo_pesado,'A','E')

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

def pageRankBli(grafo):
    G = nx.DiGraph()
    
    # --- A CORREÇÃO ENTRA AQUI ---
    # Garante que todos os nós existam no grafo, mesmo os sem links
    G.add_nodes_from(grafo.keys())
    # -----------------------------

    for origem in grafo:
        for destino in grafo[origem]:
            if G.has_edge(origem,destino):
                G[origem][destino]['peso'] +=1
            else:
                G.add_edge(origem,destino, peso=1)    
                
    resultado = nx.pagerank(G, alpha=0.85, weight='peso')
    print(resultado)

#bibliosistema
import numpy as np


def resolver_sistema_numpy(grafo_b): #errado parece
    matriz = matriz_google(grafo_b)
    n = len(matriz)
    
    # G^T - I
    G = np.array(matriz)
    A = G.T - np.identity(n)
    
    # substituindo uma linha pela equação de normalização
    A[-1, :] = 1
    b = np.zeros(n)
    b[-1] = 1
    
    v = np.linalg.solve(A, b)
    print(v)
    return v

 
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
PageRank(grafos_web11)

# # ---- Preparação (FORA do timer, igual pros dois métodos) ----
# grafo = ler_dados('teste.txt')

# # ---- Teste 1: Power Iteration (função completa, do jeito que é chamada de verdade) ----
# inicio = time.perf_counter()
# resultado_pi = PowerInteration(grafo, 0.000001, 1000)
# fim = time.perf_counter()
# print(f"Power Iteration (completo): {fim-inicio:.4f}s")

# # ---- Teste 2: NumPy solve (função completa, do jeito que é chamada de verdade) ----
# inicio = time.perf_counter()
# resultado_np = resolver_sistema_numpy(grafo)
# fim = time.perf_counter()
# print(f"NumPy solve (completo): {fim-inicio:.4f}s")