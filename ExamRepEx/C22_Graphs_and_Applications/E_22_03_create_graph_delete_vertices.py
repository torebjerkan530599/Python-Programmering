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

    # Delete the first vertex (index 0)
    graph.delete_vertex(0)
    print("\nGraph after deleting the first vertex:")
    graph.print_graph()