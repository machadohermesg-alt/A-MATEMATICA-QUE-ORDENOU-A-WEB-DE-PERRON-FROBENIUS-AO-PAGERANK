# lista = [[2,2],[1,4],[1,5]]
# n= len(lista)
# lista2=[]
# for i in range(n):
#     lista2.append(0)
#     lista2[i]= lista[i][1]
# # print(max(lista2))
# posiçao_max = (lista2.index(max(lista2)))
# print(posiçao_max)
# print(lista)    

# lista[0], lista[posiçao_max]= lista[posiçao_max],lista[0]
# print(lista)


sistema = [
        [1.0, 0, 0, 1.0],
        [0, 9, 0, 18],
        [0, 0, 8.0, 24.0]
    ]
n = 3

k=0
while k<=n-1:
        if sistema[k][k]== 0:
            maior_valor = 0      
            linha_maior=k
            for m in range(k,n):
                 if abs(sistema[m][k])>abs(maior_valor):
                      maior_valor=sistema[m][k]
                      linha_maior= m  
            sistema[k], sistema[linha_maior]= sistema[linha_maior], sistema[k]          
        # print("valor de k ",k)
        pivo= sistema[k][k]
        for i in range(k+1,n):
                
                
                # print(pivo)
                elemento = sistema[i][k]
                coefic= elemento/pivo
                for j in range(k,n+1):
                    # print(sistema[i][j])
                    if j>=k:
                        sistema[i][j]= round(-sistema[k][j]*coefic + sistema[i][j],3)
                        # print(" i = ", i, " j = ",j ," ", sistema[i][j])
        k=k+1            
for linha in sistema:
    print(linha)
print("=="*40)
vazio=[]
for i in range(n):
    default = []
    for j in range(n+1):
        default.append(0)
    vazio.append(default)
   
for i in (range(n)):
    linha_troca = n-i-1
    for j in range(n+1):
        vazio[i][j]= sistema[linha_troca][j]
    i= i +1    
# for linha in vazio:
#     print(linha) 

k = 0
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
        