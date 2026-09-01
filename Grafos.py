# Grafos teste


grafos_web1={ #dicionário chave: valor (chaves) conchetes criamos a lista
    'A': ['B','C','E'], # grafo direcionado saindo de A e indo para B E C
    'B':['C','D'],
    'C':['A','D'],
    'D': ['D','E'],
    'E': ['D']
}
grafos_web2={
    'A':['B','C'],
    'B':['B',],
    'C':['D','D'],
    'D':[]
}
grafos_web3={ #dicionário chave: valor (chaves) conchetes criamos a lista
    'A': ['B','C','E','B'], # grafo direcionado saindo de A e indo para B E C, ODNE O B É DOIS LINKS
    'B':['C','D'],
    'C':['A','D'],
    'D': ['D','E'],
    'E': ['D']
}
grafos_web4 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

# grafos_web5 -- com dangling node (página sem NENHUM link de saída)
grafos_web5 = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': []          # dangling node: D não tem nenhum link de saída
}
 
# grafos_web6 -- grafo desconectado (duas "ilhas" sem conexão entre si)
grafos_web6 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C']
    # {A,B} nunca se conecta com {C,D} -- só o damping factor resolve isso
}
 
# grafos_web7 -- caso degenerado, 1 nó só (self-loop)
grafos_web7 = {
    'A': ['A']    # único nó, aponta pra si mesmo
}
 
# grafos_web8 -- "super hub", uma página recebendo quase todos os links
grafos_web8 = {
    'A': ['E'],
    'B': ['E'],
    'C': ['E'],
    'D': ['E'],
    'E': ['A']
}
 
# grafos_web9 -- cadeia linear, sem ciclo, com dangling no final
grafos_web9 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['E'],
    'E': []       # dangling no final da cadeia
}
 
# grafos_web10 -- grafo maior e mais denso, bom pra comparar tempo
grafos_web10 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['D', 'E'],
    'D': ['A', 'B', 'E'],
    'E': ['A', 'C'],
    'F': ['A', 'B', 'C', 'D', 'E'],
    'G': ['F'],
    'H': ['F', 'G']
}
grafos_web11 ={
    'A':['A','B','C'],
    'B':['A','C','C'],
    'C':['B']
}
#print(grafos_web['A']) Saber para aonde A aponta 
grafo_pesado={
    'A':{'B':2,'C':6,'E':12,'F':2},
    'B':{'D': 3},
    'C': {'E': 2},
    'D': {'C':1,'E':6},
    'E':{},
    'F':{}
}