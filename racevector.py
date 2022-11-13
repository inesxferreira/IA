import numpy as np

#leitura e representação do circuito do ficheiro txt
file = open ('circuito.txt', 'r')
leitura = file.readlines()

arr=[]

for line in leitura:
    arr.append(line.strip()) # para remover o \n
    
#função que imprime o circuito no terminal
def imprimeCircuito(arr):
    for i  in range(0, len(arr)):
        print (arr[i])

#função que converte a lista lida do .txt numa matrix
def listaToMatriz(arr):
    x=arr
    x = [list (i) for i in x]
    #print (x)
    return [[instance for instance in sublist if not instance.isspace()] for sublist in x] #remove os espaços em branco da matriz

    
#função que retorna uma lista com os indices das posicoes da matriz para onde o jogador se pode movimentar (todas menos 'X') -- ele pode andar por 'P', '-' e 'F'
def posicoesValidas(arr):
    matriz=listaToMatriz(arr)
    lista= matriz[0]
    #print (lista)
    posicoesOk =[]
    for i in range (len(matriz)): #linhas
        for j in range (len(lista)): #colunas
            if (matriz[i][j] != 'X'): posicoesOk.append([i,j])
    print (posicoesOk)
    return posicoesOk

#função que verifica se a proxima posição é adjacente à atual
def jogadaAdjacentes(x_atual, y_atual, x_prox, y_prox):
    isOk= False
    if (x_atual == x_prox): # se a próxima jogada for na mesma linha
       if (y_prox == y_atual+1 or y_prox == y_atual-1): #posso ir direita ou esquerda
           isOk= True
    if (y_atual == y_prox): # se a próxima jogada for na mesma coluna
        if (x_prox == x_atual+1 or x_prox == x_atual-1): #posso ir descer ou subir
            isOk=True
    return isOk
    

#função que verifica se a jogada é valida
#isto é se a próxima posição não é fora pista e se é adjacente à atual
def movimentoJogadorOK(x_novo, y_novo, x_velho,y_velho):
    movimento_Valido=False
    if [x_novo,y_novo] in posicoesValidas(arr) and jogadaAdjacentes(x_novo,y_novo,x_velho,y_velho):
       movimento_Valido=True
    return movimento_Valido
    #print (movimento_Valido)
    
#array 2d que guarda o custo de cada posição
def custoPos():
    matriz=listaToMatriz(arr)
    lista = matriz[0]
    custos =[]
    for i in range (len(matriz)):
        custo=[]
        for j in range (len(lista)):
            if (matriz[i][j] != 'X'): 
                custo.append(1)
            else:  
                custo.append(25)
        custos.append(custo)
    return(custos)
 
def matrizToLista():
    matriz=listaToMatriz(arr)
    lista = matriz[0]
    listanew =[]
    for i in range (len(matriz)):
        for j in range (len(lista)):
                e= matriz[i][j]
                listanew.append(e)
    return listanew

#nao tá correto
def adj():
    matriz=listaToMatriz(arr)
    sizeLinha=len(matriz[0])# tamanho duma linha
    sizeColuna = len(matriz)#tamanho de uma coluna
    lista = custoPos()
    listaA=[]
    print (sizeLinha)
    for i in range (sizeColuna):
        for j in range ( sizeLinha):
            if (i<sizeLinha): #para a primeira linha - pq o 0%nr == 0
                tuplo=[(i,j), (i,j+1), lista[i][j+1]]
                print (tuplo)
            if (i> sizeLinha and i%sizeLinha != 0):#para a partir da segunda linha
                tuplo=[(i,j), (i,j+1), lista[i][j+1]]
                print (tuplo)
            
#imprimeCircuito(arr)
#print(listaToMatriz(arr))
#print(posicoesValidas(arr))
#print(movimentoJogadorOK(3,2,3,1))
#custoPos()
#adj()
