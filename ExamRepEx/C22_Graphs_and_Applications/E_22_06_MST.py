from queue import Queue

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __repr__(self):
        return f"({self.u}, {self.v})"

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

    def bfs_mst(self, start_index):
        search_order = []
        edge_list = []
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
                    edge_list.append(Edge(self.vertices[current_index].label, self.vertices[neighbor_index].label))

        return search_order, edge_list

    def reset_visits(self):
        for vertex in self.vertices:
            vertex.visited = False

# Test program
def main():
    # Define the adjacency matrix and corresponding vertices
    adjacency_matrix = [
        [0, 1, 1, 1, 0, 0, 0],  # A
        [0, 0, 1, 1, 1, 0, 0],  # B
        [0, 0, 0, 1, 0, 1, 0],  # C
        [0, 0, 0, 0, 1, 1, 1],  # D
        [0, 0, 0, 0, 0, 1, 1],  # E
        [0, 0, 0, 0, 0, 0, 1],  # F
        [0, 0, 0, 0, 0, 0, 0]   # G
    ]
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Create the graph
    graph = Graph(vertices, adjacency_matrix)

    # Perform BFS starting from vertex 'A' (index 0)
    bfs_result, mst_edges = graph.bfs_mst(0)

    # Print the BFS traversal order
    print("BFS Traversal Order:", ' '.join(bfs_result))
    # Print the MST edges
    print("Minimum Spanning Tree Edges:", ' '.join(map(str, mst_edges)))

if __name__ == "__main__":
    main()
