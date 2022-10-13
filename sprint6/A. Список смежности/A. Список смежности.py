def makelist(Nodes:int, Edges:int, Edge:list, num_of_Edges:list) -> list:
    for edgesIndex in range(0, int(Edges)):
        begin, end = input().split()
        if int(edgesIndex + 1) == int(begin):
            Edge.insert(int(begin), int(end))
            num_of_Edges.append(int(begin))
    return Edge, num_of_Edges

def main():
    Nodes, Edges = input().split()
    Graph = dict()
    Edge = list()
    for nodesIndex in range(1, int(Nodes) + 1):
        Graph[nodesIndex] = list()
    for edgesIndex in range(0, int(Edges)):
        Edge = list()
        begin, end = input().split()
        Edge = Graph[int(begin)]
        Edge.append(int(end))
        Graph[int(begin)] = Edge
        Edge = Graph[int(end)]
    for i in range(1, int(Nodes) + 1):
        print(len(Graph[i]),*Graph[i])


if __name__ == '__main__':
    main()