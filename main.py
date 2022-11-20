from matrix import Matriz
from arestas import Arestas
from grafo import Grafo
def main():
    #leitura e representação do circuito do ficheiro txt
    file = open ('circuito.txt', 'r')
    leitura = file.readlines()
    arr=[]
    for line in leitura:
        arr.append(line.strip()) # para remover o \n
        
    saida = -1
    matriz = Matriz()
    arestas = Arestas()
    
    while saida != 0:
        print("1 -> Gerar Circuito ")
        print("2 -> Representar pista em forma de grafo")
        print("3 -> Obter o menor caminho - algoritmo BFS")
        saida = int(input("Introduza a sua opção-> "))
        if saida == 1:
            matriz.imprimeCircuito(arr)
        if saida == 2:
            l= arestas.getEdges(arr)
            [print(i) for i in l]
            
        if saida == 3:
            n= matriz.posicoesValidas(arr)
            tamanho = len(n)
            edges= arestas.turnTupleintoNumber(arr)
            grafo = Grafo(edges, 1, tamanho)
            inicio = matriz.encontraPosicaoInicial(arr)
            fins =matriz.encontraPosicoesFinais(arr)
            fim=fins[0]
            il=str(inicio[0])
            ic=str(inicio[1])
            fl=str(fim[0])
            fc=str(fim[1])
            newi=il+ic
            newf=fl+fc
            grafo.menorCusto(grafo, int(newi), int(newf), tamanho)
            
        
        
   
if __name__ == "__main__":
    main() 
    