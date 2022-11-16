
from matrix import Matriz
# Classe nodo para definiçao dos nodos
# cada nodo tem um nome e um id, poderia ter também informação sobre um ob jeto a guardar.....
class Node():
    def __init__(self,name,x,y,custo=1):     #  construtor do nodo....."
        self.name= str(name)
        self.x=x
        self.y=y
        self.custo= custo

    def __str__(self):
        return "node " + self.name

    def __repr__(self):
        return "node " + self.name

    def setCusto(self, custo):
        self.custo = custo
    
    def setX(self,x):
        self.x=x
    
    def setY(self,y):
        self.y=y
    
    def getCusto(self):
        return self.custo

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)