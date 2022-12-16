from matrix import Matriz
from collections import defaultdict
from arestas import Arestas
import networkx as nx
from heapq import heappop, heappush
from collections import deque
import math
from dictionary import Dictionary
import numpy as np


class Informados():
    def __init__(self):
        dict = Dictionary()

    # cálculo da distância em linha reta da posição atual à posição final
    def distanciaEuclidiana(self, pAt, pFi):
        """a = np.array(pAt)
        f = np.array(pFi)
        dist = np.linalg.norm(f-a)
        """
        dist = abs(pAt[0] - pFi[0]) + abs(pAt[1] - pFi[1])

        return dist

    # dado um caminho calcula o custo total do mesmo
    def calculaCusto(self, lofl, caminho):
        custoT = 0

        # percorre o caminho resultado do algoritmo
        for n in caminho:
            if (lofl[n[0]][n[1]]) == "X":
                custoT += 25
            else:
                custoT += 1

        return custoT

    ##############
    #   Greedy   #
    ##############
    def greedy(self, dict, arr, inicio, fim):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  inicio
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([inicio])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com inicio
        parents = {}
        parent = inicio

        # velocidade inicial
        vel = (0, 0)

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

            open_list.clear()

            if n == None:
                print('Caminho não existe!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao inicio
            # seguindo o antecessor
            if n == fim:  # if n in fim
                reconstCam = []
                parents[n] = parent
                while parents[n] != n:
                    reconstCam.append(n)
                    n = parents[n]

                reconstCam.append(inicio)
                reconstCam.reverse()

                print("A procura Greedy entre a posição inicial e final é:",
                      reconstCam, "com custo", self.calculaCusto(lofl, reconstCam))

                # retorna caminho, custo
                return (reconstCam, self.calculaCusto(lofl, reconstCam))

            # todas as posições seguintes possíveis do nodo atual
            for m in dict.proxPos(lofl, arr, n, vel):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
                if m not in open_list and m not in closed_list:
                    open_list.add(m[0])
                    #parents[m[0]] = n
            parents[n] = parent
            parent = n
            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            # open_list.remove(n)
            closed_list.add(n)
            # print(open_list)
            # print("closed="+str(closed_list))
            # print("open="+str(open_list))

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
                print('Path does not exist!')
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
