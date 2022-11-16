
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

from node import Node
from matrix import Matriz


class Grafo():
    
    def __init__(self,directed=False):
        self.nodes = [] 
        self.directed = directed
        self.graph = {} # dicionario para armazenar os nodos e arestas
        self.h = {}  # dicionario para posteriormente armazenar as heuristicas para cada nodo -< pesquisa informada
        print (self.graph)
    
    #função que lê a matriz e transforma os seus elementos em nodos
    def createNodes(self,arr):
        matriz=Matriz.listaToMatriz(arr)
        lista= matriz[0]# primeira linha da matriz-- precisamos dela para saber o tamanho da linha
        for i in range (len(matriz)): #colunas
            for j in range (len(lista)): #linhas
                if (matriz[i][j] == 'X'):
                    name ="ij"
                    self.nodes.append(Node(name,i,j,25))
                else:
                    name2="ij"
                    self.nodes.append(Node(name2,i,j,1))

    #devolve nodos do grafo 
    def getNodes(self):
        return self.nodes
    
    #escrever o grafo como string
    def __str__(self):
        out = ""
        for key in self.graph.keys():
            out = out + "node" + str(key) + ": " + str(self.graph[key]) + "\n"
            return out
    
    #encontrar nodo pela posição
    def get_node_by_position(self,arr,name, x,y):
        n=Matriz.returnCustoOfaPos(arr,x,y)
        search_node = Node(name,x,y,n)
        for node in self.nodes:
            if node == search_node:
                return node
            else:
                return None

    def add_edge(self,arr,name1, x1,y1,name2,x2,y2):
        custo1=Matriz.returnCustoOfaPos(arr,x1, y1)
        custo2=Matriz.returnCustoOfaPos(arr,x2,y2)
        n1= Node(name1,x1,y1,custo1)
        n2= Node(name2,x1,y1,custo2)
        self.graph[name1].append((name1, custo2))
        if not self.directed:
            self.graph[name2].append((name2, custo1))
    
    def imprime_aresta(self):
        listaA = ""
        lista = self.graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA
    
    
    def get_arc_cost(self, name1, name2):
        custoT = math.inf
        a = self.graph[name1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == name2:
                custoT = custo

        return custoT
