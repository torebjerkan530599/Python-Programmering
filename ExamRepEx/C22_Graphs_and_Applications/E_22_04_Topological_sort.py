class Vertex:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)

class Graph:
    def __init__(self, adjacency_matrix, vertices):
        self.adjacency_matrix = adjacency_matrix
        self.vertices = vertices

    def delete_vertex(self, vertex_index):
        # Remove the vertex from the vertices list
        self.vertices.pop(vertex_index)

        # Remove the row from the adjacency matrix
        self.adjacency_matrix.pop(vertex_index)

        # Remove the column from the adjacency matrix
        for row in self.adjacency_matrix:
            row.pop(vertex_index)

    def print_graph(self):
        print("Vertices:", self.vertices)
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)

    def topological_sort(self):
        in_degree = [0] * len(self.vertices)
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix[i])):
                if self.adjacency_matrix[i][j] == 1:
                    in_degree[j] += 1

        queue = [i for i in range(len(in_degree)) if in_degree[i] == 0]
        topological_order = []

        while queue:
            vertex_index = queue.pop(0)
            topological_order.append(self.vertices[vertex_index])

            for i in range(len(self.adjacency_matrix[vertex_index])):
                if self.adjacency_matrix[vertex_index][i] == 1:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)

        if len(topological_order) == len(self.vertices):
            return topological_order
        else:
            raise Exception("The graph has at least one cycle and cannot be topologically sorted.")

# Test the implementation
if __name__ == "__main__":
    vertices = [Vertex("Agree Funding"), Vertex("Install Software"), Vertex("Planning Meeting"), Vertex("Purchase Hardware"), Vertex("Purchase Software"), Vertex("Train Users")]
    adjacency_matrix = [
        [0, 0, 0, 1, 1, 0],  # Agree Funding
        [0, 0, 0, 0, 0, 1],  # Install Software
        [1, 0, 0, 0, 0, 0],  # Planning Meeting
        [0, 1, 0, 0, 0, 0],  # Purchase Hardware
        [0, 1, 0, 0, 0, 0],  # Purchase Software
        [0, 0, 0, 0, 0, 0]   # Train Users
    ]

    graph = Graph(adjacency_matrix, vertices)
    print("Original graph:")
    graph.print_graph()

    # Perform topological sort
    try:
        topo_order = graph.topological_sort()
        print("\nTopological Sort Order:")
        for vertex in topo_order:
            print(vertex)
    except Exception as e:
        print(str(e))
