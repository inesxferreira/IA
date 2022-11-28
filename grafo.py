from matrix import Matriz
from collections import defaultdict
from matrix import Matriz
from arestas import Arestas
import networkx as nx
from collections import deque


class Grafo():

    def __init__(self, edges, x, n):
            self.adjList = [[] for _ in range(3*n)]
            for (v, u, weight) in edges:
                #se o custo for 1
                if weight == 1*x:
                    self.adjList[v].append(u)
                    
    # Função recursiva para imprimir o caminho de um dado vertice v desde o source
    def imprimeCaminho(self,predecessor, v, custo, n):
        if v >= 0:
            custo = self.imprimeCaminho(predecessor, predecessor[v], custo, n)
            custo = custo + 1
            # considera-se apenas os nodos presentes oruginalmente no grafo
            if v < n:
                print(v, end=' ')
        return custo
    
    
    # Aplica BFS no grafo começando no vertice da posição P
    def menorCusto(self,graph, source, dest, n):
        # guarda os vértices no discovered quer seja transversal ou não
        discovered = [False] * 3 * n
        # guarda a posição inicial como discovered
        discovered[source] = True
        # predecessor guarda informação sobre os predecessores.É usado para encontrar o caminho com mínimo custo desde o destino de volta ao inicio.
        predecessor = [-1] * 3 * n
        # cria uma queue para fazer BFS e enqueue o vértice inicial
        q = deque()
        q.append(source)
        # loop até a queue ser empty
        while q:
            # dequeue do nodo da frente 
            atual = q.popleft()
            # se o vértice destino é atingido
            if atual == dest:
                print(f'O caminho mais curto entre {source} e {dest} é ', end='')
                print('tendo o custo', self.imprimeCaminho(predecessor, dest, -1, n))
            # para cada aresta adjacente do vértice atual 
            for v in graph.adjList[atual]:
                if not discovered[v]:
                    # guarda como discovered e faz enqueue 
                    discovered[v] = True
                    q.append(v)
                    # set atual como o predecessor do vértice v
                    predecessor[v] = atual
    
            
    
  