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
                            return False, None  # Graph is not bipartite
        return True, colors  # Graph is bipartite

    # Return two bipartite sets if the graph is bipartite, None otherwise
    def getBipartite(self):
        is_bipartite, colors = self.isBipartite()
        if is_bipartite:
            set1 = set()
            set2 = set()
            for i, color in enumerate(colors):
                if color == 0:
                    set1.add(self.vertices[i])
                else:
                    set2.add(self.vertices[i])
            return [list(set1), list(set2)]
        else:
            return None

def main():
    vertices = [0, 1, 2, 3]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # Example edges
    graph = Graph(vertices, edges)

    bipartite_sets = graph.getBipartite()
    if bipartite_sets:
        print("Graph is bipartite.")
        print("Bipartite Sets:", bipartite_sets)
    else:
        print("Graph is not bipartite.")

if __name__ == "__main__":
    main()
