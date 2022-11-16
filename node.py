
# Classe nodo para definiçao dos nodos
# cada nodo tem um nome e um id, poderia ter também informação sobre um ob jeto a guardar.....
class Node():
    def __init__(self, name, id=-1,vel=0,a=0):     #  construtor do nodo....."
        self.m_id = id
        self.m_name = str(name)
        self.m_vel= vel
        self.m_acel=a

    def __str__(self):
        return "node " + self.m_name

    def __repr__(self):
        return "node " + self.m_name

    def setId(self, id):
        self.m_id = id
    
    def setVel(self, vel):
        self.m_vel = vel
    
    def setAcel(self, acel):
        self.m_acel = acel

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name
    
    def getVel(self):
        return self.m_vel
    
    def getAcel(self):
        return self.m_acel

    def __eq__(self, other):
        return self.m_name == other.m_name  # são iguais se nome igual, não usa o id

    def __hash__(self):
        return hash(self.m_name)