
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

from node import Node
from matrix import Matriz


class Grafo():
    
    def __init__(self,directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {} # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posteriormente armazenar as heuristicas para cada nodo -< pesquisa informada
        print (self.m_graph)
    
    
    #############
    # Escrever o grafo como string
    #############
    def addAdjencencias(self,arr):
        self.m_directed=Matriz.getListofAdjencencies(arr)
        
    #############
    # Escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
            return out

    ################################
    # Encontrar nodo pelo nome
    ################################

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None

    ##############################3
    # Imprimir arestas
    ############################333333

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    #############################
    # Adicionar   aresta no grafo
    #############################

    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if (n1 not in self.m_nodes):
            self.m_nodes.append(n1)
            self.m_graph[node1] = list()
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.m_nodes):
            self.m_nodes.append(n2)
            self.m_graph[node2] = list()
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[node1].append((node2, weight))


        if not self.m_directed:
            self.m_graph[node2].append((node1, weight))


    #############################
    # Devolver nodos do Grafo
    ############################

    def getNodes(self):
        return self.m_nodes

    ###############################
    # Devolver o custo de uma aresta
    ################################

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    ##############################
    #  Dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            #print(teste[i])
            i = i + 1
        return custo

    #####################################################
    # Procura BFS
    ######################################################

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)



        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    ###################################################
    # Função   getneighbours, devolve vizinhos de um nó
    ####################################################

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    ###############################
    #  Desenha grafo  modo grafico
    ###############################

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ##########################################################################
    #  add_heuristica   -> define heuristica para cada nodo
    ##########################################################################

    def add_heuristica(self, n, estima):
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estima



    #######################################################################
    #    heuristica   -> define heuristica para cada nodo 1 por defeito....
    #    apenas para teste de pesquisa informada
    #######################################################################

    def heuristica(self):
        nodos = self.m_graph.keys
        for n in nodos:
            self.m_h[n] = 1
        return (True)


    ##########################################3
    #
    def calcula_est(self, estima):
        l = list(estima.keys())
        min_estima = estima[l[0]]
        node = l[0]
        for k, v in estima.items():
            if v < min_estima:
                min_estima = v
                node = k
        return node


    ###################################3
    # devolve heuristica do nodo
    ####################################

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])

