from queue import Queue

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

class Graph:
    def __init__(self, vertices=[], adjacency_matrix=[]):
        self.vertices = [Vertex(label) for label in vertices]
        self.adjacency_matrix = adjacency_matrix
        self.neighbors = self.get_adjacency_lists(adjacency_matrix)

    def get_adjacency_lists(self, adjacency_matrix):
        neighbors = []
        for i in range(len(adjacency_matrix)):
            neighbors.append([])
            for j in range(len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] == 1:
                    neighbors[i].append(j)
        return neighbors

    def bfs(self, start_index):
        search_order = []
        queue = Queue()
        self.vertices[start_index].visited = True
        queue.put(start_index)

        while not queue.empty():
            current_index = queue.get()
            search_order.append(self.vertices[current_index].label)

            for neighbor_index in self.neighbors[current_index]:
                if not self.vertices[neighbor_index].visited:
                    self.vertices[neighbor_index].visited = True
                    queue.put(neighbor_index)

        return search_order

# Test program
def main():
    # Define the adjacency matrix and corresponding vertices
    adjacency_matrix = [
        [0, 1, 0, 0, 1, 0, 0],  # A
        [0, 0, 1, 0, 0, 0, 0],  # B
        [0, 0, 0, 1, 0, 0, 0],  # C
        [0, 0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 1, 0],  # E
        [0, 0, 0, 0, 0, 0, 1],  # F
        [0, 0, 0, 0, 0, 0, 0]   # G
    ]
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Create the graph
    graph = Graph(vertices, adjacency_matrix)

    # Perform BFS starting from vertex 'A' (index 0)
    bfs_result = graph.bfs(0)

    # Print the BFS traversal order
    print("BFS Traversal Order:", ' '.join(bfs_result))

if __name__ == "__main__":
    main()
