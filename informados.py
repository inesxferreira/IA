from matrix import Matriz
from collections import defaultdict
from arestas import Arestas
import networkx as nx
from heapq import heappop, heappush
from collections import deque
import math
from dictionary import Dictionary

class Informados():
    def __init__(self):
        dict = Dictionary()

    # cálculo da distância em linha reta da posição atual à posição final
    def distanciaEuclidiana(self, pAt, pFi):
        dist = abs(pAt[0] - pFi[0]) + abs(pAt[1] - pFi[1])
        return dist

    # dado um caminho calcula o custo total do mesmo
    def calculaCusto(self, lofl, caminho):
        custoT = 0

        # percorre o caminho resultado do algoritmo
        for n in caminho:
            #verifica se é parede
            if (lofl[n[0]][n[1]]) == "X":
                custoT += 25
            else:
                #ou pista
                custoT += 1

        return custoT

    # verifica se o salto entre duas posições é possível, se tiver paredes pelo meio dá uma alternativa
    def validaSalto (self,grafo,pI,pF,vel):
        #validar o caminho entre pI e pF
        #posição inicial
        parent = pI
        currpos = (0,0)
        if vel[0] > 0:
            x = -1
        else: x = 1
        if vel[1] > 0:
            y = -1
        else: y = 1
        print("parent is ",parent)
        decrementer = (x,y)
        while parent != pF:
        #procurar próximo nodo consoante a velocidade
            if vel[0] != 0:
                currpos[0] = parent[0] + vel[0]
                vel[0] = vel[0] + decrementer[0]
            if vel[1] != 0:
                currpos[1] = parent[1] + vel[1]
                vel[1] = vel[1] + decrementer[1]
            if vel != (0,0):
                currset = grafo[parent]
                if currpos in currset:
                    parent = currpos
            else: return None
        #retornar a posição válida
        return parent

    ##############
    #   Greedy   #
    ##############
    def greedy(self, dict, grafo, arr, inicio, fim):
        # lista de nodos visitados, mas com vizinhos que ainda não foram todos visitados, começa com o  inicio
        open_list = set([inicio])
        # lista de nodos visitados mas vizinhos também já foram visitados
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor(parent) de um nodo
        parents = {}
        parent = inicio

        # velocidade inicial
        vel = (0, 0)

        #lista de listas que representam o circuito como uma matriz
        lofl = dict.listaToM(arr)

        while len(open_list) > 0:
            n = None
            menor = 1000.0
            # encontrar nodo com a menor heuristica
            for i in open_list:
                d = self.distanciaEuclidiana(i, fim)

                if (d <= menor):  # guardar o valor com a menor distancia ao fim
                    menor = d
                    n = i

            #limpa todos os nodos presentes na open list
            open_list.clear()

            if n == None:
                print('Caminho não existe!')
                return None
            
            #se o nodo em questão não for filho do parent 
            if n not in dict.proxPos(lofl, arr, parent, vel):
                vel = (0,0)
            else: 
                vel = (n[0]-parent[0],n[1]-parent[1]) #atribuir velocidade ao jogador
            #print(vel)
            
            # se o nodo corrente é o destino
            if n == fim:  # if n in fim
                reconstCam = []
                parents[n] = parent
                while parents[n] != n:
                    #reconstruir caminho até ao nodo inicial
                    reconstCam.append(n)
                    #marcar o antecessor do nodo para a próxima iteração
                    n = parents[n]

                reconstCam.append(inicio)
                reconstCam.reverse()

                print("A procura Greedy entre a posição inicial e final é:",
                      reconstCam, "com custo", self.calculaCusto(lofl, reconstCam))

                # retorna caminho, custo
                return (reconstCam, self.calculaCusto(lofl, reconstCam))

            # todas as posições seguintes possíveis do nodo atual
            for m in dict.proxPos(lofl, arr, n, vel):                
                # Se o nodo corrente nao está na closed list, marcar o seu antecessor
                if (m not in closed_list):
                    print(self.validaSalto(grafo,parent,m[0],vel))
                    open_list.add(m[0])
                    #parents[m[0]] = n
            parents[n] = parent
            parent = n
            # adicionar à closed_list todos os seus vizinhos foram inspecionados
            # open_list.remove(n)
            closed_list.add(n)

        print('Caminho não existe!')
        return None

    ##############
    #     A*     #
    ##############
    def procura_aStar(self, start, end):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}  # g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start
        n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.getH(v)
            if flag == 1:
                min_estima = self.calcula_est(calc_heurist)
                n = min_estima
            if n == None:
                print('Caminho não existe!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                #print('Path found: {}'.format(reconst_path))
                return (reconst_path, self.calcula_custo(reconst_path))

            # for all neighbors of the current node do
            # definir função getneighbours  tem de ter um par nodo peso
            for (m, weight) in self.getNeighbours(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
