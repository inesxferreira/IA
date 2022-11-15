import queue
class Matriz():
    
    #função que imprime o circuito no terminal
    def imprimeCircuito(self,arr):
        for i  in range(0, len(arr)):
            print (arr[i])

    #função que converte a lista lida do .txt numa matrix
    def listaToMatriz(self,arr):
        x=arr
        x = [list (i) for i in x]
        #print (x)
        return [[instance for instance in sublist if not instance.isspace()] for sublist in x] #remove os espaços em branco da matriz


    #funcao que retorna as coordenadas da posicao inicial
    def encontraPosicaoInicial(self,arr):
        inicio =()
        matriz=self.listaToMatriz(arr)
        lista= matriz[0]
        for i in range (len(matriz)): #colunas
            for j in range (len(lista)): #linhas
                if (matriz[i][j] == 'P'): inicio=(i,j)
        return (inicio)

    #funcao que retorna as coordenadas das possíveis metas
    def encontraPosicoesFinais (self,arr):
        matriz=self.listaToMatriz(arr)
        lista= matriz[0]# primeira linha da matriz-- precisamos dela para saber o tamanho da linha
        #print (lista)
        finais =[]
        for i in range (len(matriz)): #colunas
            for j in range (len(lista)): #linhas
                if (matriz[i][j] == 'F'): finais.append([i,j])
        return finais


    #função que retorna uma lista com os indices das posicoes da matriz para onde o jogador se pode movimentar (todas menos 'X') -- ele pode andar por 'P', '-' e 'F'
    def posicoesValidas(self,arr):
        matriz=self.listaToMatriz(arr)
        lista= matriz[0]# primeira linha da matriz-- precisamos dela para saber o tamanho da linha
        #print (lista)
        posicoesOk =[]
        for i in range (len(matriz)): #colunas
            for j in range (len(lista)): #linhas
                if (matriz[i][j] != 'X'): posicoesOk.append([i,j])
        #print (posicoesOk)
        return posicoesOk

    #função que verifica se a proxima posição é adjacente à atual
    def jogadaAdjacentes(self,x_atual, y_atual, x_prox, y_prox):
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
    def movimentoJogadorOK(self,x_novo, y_novo, x_velho,y_velho,arr):
        movimento_Valido=False
        if [x_novo,y_novo] in self.posicoesValidas(arr) and self.jogadaAdjacentes(x_novo,y_novo,x_velho,y_velho):
            movimento_Valido=True
        return movimento_Valido
        #print (movimento_Valido)
        
    #array 2d que guarda o custo de cada posição
    def custoPos(self,arr):
        matriz=self.listaToMatriz(arr)
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
    
    #numa dada posição, desde que seja válido, podemos: 
    #avançar para a esquerda(y-1), para a direita(y+1)
    #avançar para cima (x-1), para baixo (x+1)
    #avançar esquerda e cima em simultaneo(y-1 e x-1) - diagonal
    #avançar direita e cima em simultaneo(y+1 e x-1) - diagonal
    #avançar esquerda e baixo em simultaneo(y-1 e x+1) - diagonal
    #avançar direita e baixo em simultaneo(y+1 e x+1) - diagonal
    def adjentOfPos(self,arr,x_atual,y_atual):
        list=[]
        if ([x_atual-1,y_atual]) in self.posicoesValidas(arr): list.append((x_atual-1,y_atual))
        if ([x_atual+1,y_atual]) in self.posicoesValidas(arr): list.append((x_atual+1,y_atual))
        if ([x_atual,y_atual-1]) in self.posicoesValidas(arr):list.append((x_atual,y_atual-1))
        if ([x_atual,y_atual+1]) in self.posicoesValidas(arr):list.append((x_atual,y_atual+1))
        if ([x_atual-1,y_atual-1]) in self.posicoesValidas(arr):list.append((x_atual-1,y_atual-1))
        if ([x_atual+1,y_atual-1]) in self.posicoesValidas(arr):list.append((x_atual+1,y_atual-1))
        if ([x_atual-1,y_atual+1]) in self.posicoesValidas(arr):list.append((x_atual-1,y_atual+1))
        if ([x_atual+1,y_atual+1]) in self.posicoesValidas(arr):list.append((x_atual+1,y_atual+1))
        #retorna a lista das posições adjacentes a uma dada cordenada
        return(list)
              
    #retorna um tuplo em que o 1 elem é uma dada posição e o 2 elem é a lista de posicoes válidas adjacentes a essa posição
    def getListofAdjencencies(self,arr):
        matriz=self.listaToMatriz(arr)
        lista = matriz[0]
        newAdjs=[]
        for i in range (len(matriz)): #colunas
            for j in range (len(lista)): #linhas
                newAdjs.append([(i,j),self.adjentOfPos(arr,i,j)])
        print (newAdjs)
                          
    #imprimeCircuito(arr)
    #print(listaToMatriz(arr))
    #encontraPosicaoInicial(arr)
    #encontraPosicoesFinais(arr)

    #print(posicoesValidas(arr))
    #print(movimentoJogadorOK(3,2,3,1))
    #custoPos()
    #adj()
