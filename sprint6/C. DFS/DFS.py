def dfs(Graph:dict, Nodes:int, startnode: int, visited: list, stack: list, result: list) -> list:
    while stack:
        Node = stack.pop(0)
        if visited[int(Node) - 1] is False:
            result.append(Node)
            visited.pop(int(Node) - 1)
            visited.insert((int(Node) - 1), True)

    for number in Graph[int(startnode)]:
        if visited[number - 1] is False:
            stack.append(number)
            dfs(Graph, Nodes, int(number), visited, stack, result)
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
        Graph[int(begin)] = sorted(Edge)
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
    print(*dfs(Graph, Nodes, int(startnode), visited, stack, result))


if __name__ == '__main__':
    main()