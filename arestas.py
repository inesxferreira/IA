# Python program for 
# validation of a graph
  
# import dictionary for graph
from matrix import Matriz
from collections import defaultdict
import networkx as nx

class Arestas():
    
    # adiciona uma aresta ao grafo
    graph = defaultdict(list)
    weights = {}
    
    def addEdge(self,arr,graph,u,v):
        matriz = Matriz()
        custo = matriz.returnCustoOfaPos(arr,v)
        nodeCost = (v,custo)
        graph[u].append(nodeCost)
         
    #gera arestas
    def generate_edges(self,graph):
        edges = []
        for node in graph:
            for neighbour in graph[node]:
                edges.append((node, neighbour))
        return edges
    
    # deeclarar o dicionário como grafo
    def dictToGraph(self,arr):
        matriz = Matriz()
        dict = matriz.getListofAdjencencies(arr)
        for key, values in dict.items():
            chave =key
            if(isinstance(values, list)):
                for value in values:
                    self.addEdge(arr,self.graph,chave,value) 
            else:  self.addEdge(arr,self.graph,chave,value)
        print (self.generate_edges(self.graph))
         