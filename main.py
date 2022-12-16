from matrix import Matriz
from arestas import Arestas
from dictionary import Dictionary
from naoInformados import NaoInformados
from informados import Informados
        
def main():
    #leitura e representação do circuito do ficheiro txt
    file1 = open ('./circuitos/circuito.txt', 'r')
    file2 = open ('./circuitos/circuito1.txt', 'r')
    file3 = open ('./circuitos/circuito2.txt', 'r')
    file4 = open ('./circuitos/circuito3.txt', 'r')
    leitura = file1.readlines()
    leitura1 = file2.readlines()
    leitura2 = file3.readlines()
    leitura3 = file4.readlines()
    
    arr=[]
    for line in leitura:
        arr.append(line.strip()) # para remover o \n
    
    arr1=[]
    for line in leitura1:
        arr1.append(line.strip()) # para remover o \n
    
    arr2=[]
    for line in leitura2:
        arr2.append(line.strip()) # para remover o \n
    
    arr3=[]
    for line in leitura3:
        arr3.append(line.strip()) # para remover o \n
        
    saida = -1
    matriz = Matriz()
    arestas = Arestas()
    dict= Dictionary()

    
    while saida != 0:
        print (" ########## BEM VINDO AO VECTOR RACE  ##########")
        print ("Comece por selecionar um circuito de entre os circuitos disponiveis")
        print("1 ->  Circuito 1 ")
        print("2 ->  Circuito 2" )
        print("3 ->  Circuito 3 ")
        print("4 ->  Circuito 4 ")
        print("0 -> Sair do Programa")
        print (" ###############################################")
        saida = int(input("Escolha o circuito que pretende-> "))
        if saida == 1:
            saida2= -1
            while saida2 !=0:
                print("########## SELECIONOU O CIRCUITO 1  ##########" )
                print("1 -> Gerar o Circuito ")
                print("2 -> Representar a pista em forma de grafo")
                print("3 -> Pesquisa DFS")
                print("4 -> Pesquisa BFS")
                print("5 -> Pesquisa Greedy")
                print("0 ->  Voltar ao menu")
                print("##############################################" )
                saida2 = int(input("Introduza a sua opção-> "))
                if saida2 == 1:
                         matriz.imprimeCircuito(arr)
                if saida2 == 2:
                        l= arestas.getEdges(arr)
                        [print(i) for i in l]   
                if saida2 == 3:
                        inicio = matriz.encontraPosicaoInicial(arr)
                        fins = matriz.encontraPosicoesFinais(arr)
                        grafo = NaoInformados(arr)
                        path =[]
                        visited = set()
                        mylist =[]
                        for i in fins:
                            path2 =[]
                            visited2 = set()
                            f= grafo.verificaDFSfins(inicio,i,path2,visited2)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_DFS(inicio,dest,path,visited)
                        print(caminho)
                if saida2 == 4:
                        inicio = matriz.encontraPosicaoInicial(arr)
                        fins = matriz.encontraPosicoesFinais(arr)
                        grafo = NaoInformados(arr)
                        mylist=[]
                        for i in fins:
                            f= grafo.verificaBFSfins(inicio,i)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_BFS(inicio,dest)
                        print(caminho)
                if saida2 == 5:
                        inicio = matriz.encontraPosicaoInicial(arr)
                        grafo = dict.makeGrafo(arr, inicio)
                        fins = matriz.encontraPosicoesFinais(arr)
                        inf = Informados()
                        greedy = inf.greedy(dict, grafo, arr, inicio, fins[0])

        if saida == 2:
            saida2= -1
            while saida2 !=0:
                print("########## SELECIONOU O CIRCUITO 2  ##########" )
                print("1 -> Gerar o Circuito ")
                print("2 -> Representar a pista em forma de grafo")
                print("3 -> Pesquisa DFS")
                print("4 -> Pesquisa BFS")
                print("0 ->  Voltar ao menu")
                print("##############################################" )
                saida2 = int(input("Introduza a sua opção-> "))
                if saida2 == 1:
                         matriz.imprimeCircuito(arr1)
                if saida2 == 2:
                        l= arestas.getEdges(arr1)
                        [print(i) for i in l]   
                if saida2 == 3:
                        inicio = matriz.encontraPosicaoInicial(arr1)
                        fins = matriz.encontraPosicoesFinais(arr1)
                        grafo = NaoInformados(arr1)
                        path =[]
                        visited = set()
                        mylist =[]
                        for i in fins:
                            path2 =[]
                            visited2 = set()
                            f= grafo.verificaDFSfins(inicio,i,path2,visited2)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_DFS(inicio,dest,path,visited)
                        print(caminho)
                if saida2 == 4:
                        inicio = matriz.encontraPosicaoInicial(arr1)
                        fins = matriz.encontraPosicoesFinais(arr1)
                        grafo = NaoInformados(arr1)
                        mylist=[]
                        for i in fins:
                            f= grafo.verificaBFSfins(inicio,i)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_BFS(inicio,dest)
                        print(caminho)
                if saida2 == 6:
                        inicio = matriz.encontraPosicaoInicial(arr1)
                        t = dict.makeGrafo(arr1, inicio)
                        fins = matriz.encontraPosicoesFinais(arr1)
                        inf = Informados()
                        greedy = inf.greedy(dict, arr1, inicio, fins[0])
                        print(greedy)
        if saida == 3:
            saida2= -1
            while saida2 !=0:
                print("########## SELECIONOU O CIRCUITO 3  ##########" )
                print("1 -> Gerar o Circuito ")
                print("2 -> Representar a pista em forma de grafo")
                print("3 -> Pesquisa DFS")
                print("4 -> Pesquisa BFS")
                print("0 ->  Voltar ao menu")
                print("##############################################" )
                saida2 = int(input("Introduza a sua opção-> "))
                if saida2 == 1:
                         matriz.imprimeCircuito(arr2)
                if saida2 == 2:
                        l= arestas.getEdges(arr2)
                        [print(i) for i in l]   
                if saida2 == 3:
                        inicio = matriz.encontraPosicaoInicial(arr2)
                        fins = matriz.encontraPosicoesFinais(arr2)
                        grafo = NaoInformados(arr2)
                        path =[]
                        visited = set()
                        mylist =[]
                        for i in fins:
                            path2 =[]
                            visited2 = set()
                            f= grafo.verificaDFSfins(inicio,i,path2,visited2)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_DFS(inicio,dest,path,visited)
                        print(caminho)
                if saida2 == 4:
                        inicio = matriz.encontraPosicaoInicial(arr2)
                        fins = matriz.encontraPosicoesFinais(arr2)
                        grafo = NaoInformados(arr2)
                        mylist=[]
                        for i in fins:
                            f= grafo.verificaBFSfins(inicio,i)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_BFS(inicio,dest)
                        print(caminho)
                if saida2 == 6:
                        inicio = matriz.encontraPosicaoInicial(arr1)
            
                        t = dict.makeGrafo(arr1, inicio)
                        print(t)
        if saida == 4:
            saida2= -1
            while saida2 !=0:
                print("########## SELECIONOU O CIRCUITO 4  ##########" )
                print("1 -> Gerar o Circuito ")
                print("2 -> Representar a pista em forma de grafo")
                print("3 -> Pesquisa DFS")
                print("4 -> Pesquisa BFS")
                print("0 ->  Voltar ao menu")
                print("##############################################" )
                saida2 = int(input("Introduza a sua opção-> "))
                if saida2 == 1:
                         matriz.imprimeCircuito(arr3)
                if saida2 == 2:
                        l= arestas.getEdges(arr3)
                        [print(i) for i in l]   
                if saida2 == 3:
                        inicio = matriz.encontraPosicaoInicial(arr3)
                        fins = matriz.encontraPosicoesFinais(arr3)
                        grafo = NaoInformados(arr3)
                        path =[]
                        visited = set()
                        mylist =[]
                        for i in fins:
                            path2 =[]
                            visited2 = set()
                            f= grafo.verificaDFSfins(inicio,i,path2,visited2)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_DFS(inicio,dest,path,visited)
                        print(caminho)
                if saida2 == 4:
                        inicio = matriz.encontraPosicaoInicial(arr3)
                        fins = matriz.encontraPosicoesFinais(arr3)
                        grafo = NaoInformados(arr3)
                        mylist=[]
                        for i in fins:
                            f= grafo.verificaBFSfins(inicio,i)
                            mylist.append(f)
                        menor = 10000
                        dest =(0,0)
                        for i in mylist:
                            if (i[1] < menor): 
                                dest = i[0]
                                menor = i[1]
                        caminho =grafo.procura_BFS(inicio,dest)
                        print(caminho)
                if saida2 == 6:
                        inicio = matriz.encontraPosicaoInicial(arr1)
            
                        t = dict.makeGrafo(arr1, inicio)
                        print(t) 

if __name__ == "__main__":
    main() 
    
