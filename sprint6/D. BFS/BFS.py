def bfs(Graph:dict, Nodes:int, startnode: int, visited: list, stack: list, result: list) -> list:
    visited.pop(int(startnode) - 1)
    visited.insert((int(startnode) - 1), True)
    while stack:
        Node = stack.pop(0)
        result.append(Node)
        for number in Graph[int(Node)]:
            if visited[number - 1] is False:
                visited.pop(int(number) - 1)
                visited.insert((int(number) - 1), True)
                stack.append(number)
    return result

def main():
    Nodes, Edges = input().split()
    Graph = dict()
    Edge = list()
    for nodesIndex in range(1, int(Nodes) + 1):
        Graph[nodesIndex] = list()
    for edgesIndex in range(0, int(Edges)):
        begin, end = input().split()
        Edge = Graph[int(begin)]
        Edge.append(int(end))
        Graph[int(begin)] = Edge
        Edge = Graph[int(end)]
        if begin not in Edge:
            Edge.append(int(begin))
        Graph[int(end)] = sorted(Edge)
    startnode = input()
    stack = [] * int(Nodes)
    stack.append(int(startnode))
    visited = [] * int(Nodes)
    visited = [False for i in range(1, int(Nodes) + 1)]
    result = list()
    print(*bfs(Graph, Nodes, int(startnode), visited, stack, result))


if __name__ == '__main__':
    main()