from pathlib import Path


class Graph:
    def __init__(self):
        self.vertices = []
        self.neighbors = []

    def add_vertex(self, v):
        self.vertices.append(v)
        self.neighbors.append([])

    def add_edge(self, u, v):
        self.neighbors[u].append(Edge(v))
        self.neighbors[v].append(Edge(u))

    def printEdges(self):
        for u in range(len(self.neighbors)):
            print(f"{u}:", end=" ")
            for e in self.neighbors[u]:
                print(f"({u}, {e.v})", end=" ")
            print()

    def dfs(self, v):
        searchOrders = []
        parent = [-1] * len(self.vertices)
        isVisited = [False] * len(self.vertices)
        self.dfsHelper(v, parent, searchOrders, isVisited)
        return Tree(v, parent, searchOrders, self.vertices)

    def dfsHelper(self, v, parent, searchOrders, isVisited):
        searchOrders.append(v)
        isVisited[v] = True
        for e in self.neighbors[v]:
            w = e.v
            if not isVisited[w]:
                parent[w] = v
                self.dfsHelper(w, parent, searchOrders, isVisited)


class Edge:
    def __init__(self, v):
        self.v = v


class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root
        self.parent = parent
        self.searchOrders = searchOrders
        self.vertices = vertices

    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)


def read_graph_from_file(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        for i in range(n):
            graph.add_vertex(i)
        for line in file:
            data = list(map(int, line.split()))
            u = data[0]
            for v in data[1:]:
                graph.add_edge(u, v)
    return graph


def is_graph_connected(graph):
    if len(graph.vertices) == 0:
        return True  # An empty graph is considered connected.
    tree = graph.dfs(0)
    return tree.getNumberOfVerticesFound() == len(graph.vertices)


def main():
    #file_path = input("Enter the path of the file containing the graph: ").strip()
    file_path = Path(__file__).parent / 'connected_graph.txt'
    graph = read_graph_from_file(file_path)
    graph.printEdges()
    if is_graph_connected(graph):
        print("The graph is connected.")
    else:
        print("The graph is not connected.")


if __name__ == "__main__":
    main()
