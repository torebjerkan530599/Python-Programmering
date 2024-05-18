from queue import Queue

class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges 
    def getAdjacencyLists(self, edges):
        neighbors = [[] for _ in range(len(self.vertices))]
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)  # Assuming undirected graph
        return neighbors

    # Return True if the graph is bipartite, False otherwise
    def isBipartite(self):
        colors = [-1] * len(self.vertices)  # Initialize colors

        # Perform BFS traversal
        for start_vertex in range(len(self.vertices)):
            if colors[start_vertex] == -1:
                colors[start_vertex] = 0  # Color the start vertex with 0
                queue = Queue()
                queue.put(start_vertex)

                while not queue.empty():
                    u = queue.get()
                    for v in self.neighbors[u]:
                        if colors[v] == -1:
                            colors[v] = 1 - colors[u]  # Assign alternate color to neighbor
                            queue.put(v)
                        elif colors[v] == colors[u]:
                            return False  # Graph is not bipartite if adjacent vertices have same color
        return True  # Graph is bipartite

    # Other methods...

def main():
    vertices = [0, 1, 2, 3]
    edges1 = [(0, 1), (0, 3), (1, 2), (2, 3)]  # Example edges
    graph1 = Graph(vertices, edges1)

    print("Graph is bipartite:", graph1.isBipartite())
    
    edges2 = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]  # Adding an edge within the same set
    graph2 = Graph(vertices, edges2)
    print("Graph is bipartite:", graph2.isBipartite())

if __name__ == "__main__":
    main()
