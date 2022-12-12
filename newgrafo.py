from os import nice
from matrix import Matriz
from collections import defaultdict
from arestas import Arestas
import networkx as nx
import sys #sys.maxsize reports the platform's pointer size
from heapq import heappop, heappush
from collections import deque
import math


#Classe que guarda os Nodos da Heap
class Nodo:
    def __init__(self, vertice, peso=0):
            self.vertice = vertice
            self.peso = peso

 #função que faz a operação less-than
    def __lt__(self, other):
        return self.peso < other.peso

#classe para representar o grafo
class oGrafo:

    def __init__(self, edges, n):
            #aloca memória para a lista de adjacencias
            self.listaAdjacencias = [[] for _ in range(n)]
            #adiciona arestas ao grafo - orientadas 
            for (source, dest, peso) in edges:
                self.listaAdjacencias[source].append((dest, peso))
    
    #função auxiliar para encontrar o caminho entre um nó e outro            
    def get_caminho(self,prev, i, caminho):
            if i >= 0:
                self.get_caminho(prev, prev[i], caminho)
                caminho.append(i)

    #aplica o algoritmo de Dijktra no grafo fornecido
    def encontraCaminhoMaisCurto(self,graph, source,fins, n):
        #cria uma heap minima e faz pushcaminho da origem com distância a 0
        list = []
        heappush(list, Nodo(source))
        dist = [sys.maxsize] * n # a distância inicial desde a origem até ao vertice como infinita para já
        dist[source] = 0 #a distância da origem a si mesma é 0
        #lista que permite verificar se o custo mínimo já foi alcançado
        terminou = [False] * n
        terminou[source] = True
        prev = [-1] * n #guarda o nodo antecessor
        while list: #ciclo até a heap ficar vazia
            node = heappop(list) #remove e retorna o melhor vértice
            u = node.vertice  #get do vertice    
            #para cada nodo adjacente 
            for (v, peso) in graph.listaAdjacencias[u]:
                if not terminou[v] and (dist[u] + peso) < dist[v]:
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    heappush(list, Nodo(v, dist[v]))
            #o vértice foi visitado, já não vamos selecioná-lo outra vez
            terminou[u] = True
        
        caminho = []
        custo = 100
        custos=[]
    
        for i in range(n):
            if i != source and dist[i] != sys.maxsize and i in fins:
                self.get_caminho(prev, i, caminho)
                custos.append(dist[i])
                caminho.clear()
        #print (custos)
        minimum = min(custos)
        verify = custos.count(minimum)
        found = 0
        for i in range(n): #se só houver um caminho mínimo
            if i != source and dist[i] != sys.maxsize and i in fins:
                caminho.clear()
                self.get_caminho(prev, i, caminho)
                if dist[i] == min(custos) and verify== 1: #se houver apenas um caminho com o custo mínimo
                    print (verify)
                    print(f'O caminho mais curto entre {source} e {i}, com custo = {dist[i]},  é = {caminho}')
                    caminho.clear() #limpa todas as entradas de uma lista
                elif dist[i] == min(custos) and verify>1 and found == 0: # se houver mais do que um caminho com o custo mínimo
                    found = 1 #imprime o 1 caminho
                    print(f'O caminho mais curto entre {source} e {i}, com custo = {dist[i]},  é = {caminho}')

    #dado um caminho calcula o seu custo
    def calcula_custo(self, matriz,caminho):
        teste = caminho # caminho é uma lista de nodos
        custo = 0
        i = 0
        while i + 1 < len(teste):
            #custo = custo + matriz.returnCustoOfaPos(teste, teste[i])
            custo = custo + 1
            # print(teste[i])
            i = i + 1
        return custo

    #cálculo da distância em linha reta da posição atual à posição final
    def distanciaEuclidiana(self, pAt, pFi):
        differences = [pAt[x] - pFi[x] for x in range(len(pAt))]
        differences_squared = [difference ** 2 for difference in differences]
        sum_of_squares = sum(differences_squared)
        return sum_of_squares ** 0.5

    #dado a posição atual do jogador, verifica quais as próximas posições possíveis
    def verificaProxPos(self, arr, matriz,posAt, posF):
        velJogador = (0, 0) #velocidade inicial é 0 
        #todas as 9 possibilidades de aceleração
        possibilidades = [(-1, -1), (-1, 0), (-1, 1), (0, 0),(0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]
        posNovas = [] #lista de posições possíveis após o cálculo da velocidade 
        velSeguintes = [] #lista de velocidades seguintes possíveis

        menorDist = 0 #guarda o menor valor da distância à posição final
        menorPos = (0,0) #vai atualizar qual o nodo com menor distância à posição final

        # vai testar as 9 posicoes de acel
        for acel in possibilidades:
            velNova = (velJogador[0] + acel[0], velJogador[1] + acel[1]) #cálculo da velocidade seguinte
            posNova = (velNova[0] + posAt[0], velNova[1] + posAt[1]) #cálculo da posição seguinte
            posNovas.append(posNova) #posição seguinte é adicionada ao conjunto de posições possíveis
            velSeguintes.append(velNova) #adiciona à lista as velocidades seguintes


        #na lista de posições possíveis, verifica qual delas tem menor distância até à posição final
        for p in posNovas:
            custoPos = matriz.returnCustoOfaPos(arr,p)

            if (custoPos == 25): #se a posição atual é parede
                velJogador = (0,0)
                print("É parede")
            else:
                if (menorDist > self.distanciaEuclidiana(p, posF)): 
                    menorDist = self.distanciaEuclidiana(p, posF)
                    menorPos = p  # atualiza o nodo que tem menor distância até à posição final
                    velJogador = velSeguintes[p] #atualiza a velocidade do jogador

        return menorPos


    # aplica o algoritmo Greedy no grafo fornecido
    def greedy(self, arr, matriz,inicio, fim):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  inicio
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([inicio])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com inicio
        parents = {}
        parents[inicio] = inicio

        while len(open_list) > 0:
            n = None

            # encontrar nodo com a menor heuristica
            for i in open_list:

                n = self.verificaProxPos(arr,matriz,i,fim)

            if n == None:
                print('Path does not exist!')
                return None
            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao inicio
            # seguindo o antecessor
            if n == fim: #if n in fim
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(inicio)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(matriz,reconst_path))


           ####### if n in self.keys():
                # para todos os vizinhos  do nodo atual 
                    for m in matriz.adjentOfPos(arr,n[0],n[1]): #vai buscar os adjacentes da posição à matriz
                        # Se o nodo corrente nao esta na open nem na closed list
                        # adiciona-lo à open_list e marcar o antecessor
                            if m not in open_list and m not in closed_list:
                                open_list.add(m)
                                parents[m] = n

            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None