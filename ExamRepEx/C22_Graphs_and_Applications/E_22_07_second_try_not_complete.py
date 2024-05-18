class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __repr__(self):
        return f"({self.u}, {self.v})"

class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self, vertices=[], adjacency_matrix_with_cycles=[]):
        self.vertices = [Vertex(label) for label in vertices]
        self.adjacency_matrix_with_cycles = adjacency_matrix_with_cycles
        self.neighbors = self.get_adjacency_lists(adjacency_matrix_with_cycles)

    def get_adjacency_lists(self, adjacency_matrix_with_cycles):
        neighbors = []
        for i in range(len(adjacency_matrix_with_cycles)):
            neighbors.append([])
            for j in range(len(adjacency_matrix_with_cycles[i])):
                if adjacency_matrix_with_cycles[i][j] == 1:
                    neighbors[i].append(j)
        return neighbors

    def bfs_mst(self, start_index):
        search_order = []
        edge_list = []
        visited = set()
        queue = [start_index]
        visited.add(start_index)

        while queue:
            current_index = queue.pop(0)
            search_order.append(self.vertices[current_index].label)

            for neighbor_index in self.neighbors[current_index]:
                if neighbor_index not in visited:
                    visited.add(neighbor_index)
                    queue.append(neighbor_index)
                    edge_list.append(Edge(self.vertices[current_index].label, self.vertices[neighbor_index].label))

        return search_order, edge_list

    def getACycle(self):
        visited = set()
        for start_index in range(len(self.vertices)):
            cycle = self._dfs_cycle_detection(start_index, -1, visited)
            if cycle:
                return cycle
        return None

    def _dfs_cycle_detection(self, current_index, parent_index, visited):
        if current_index in visited:
            return [current_index]

        visited.add(current_index)

        for neighbor_index in self.neighbors[current_index]:
            if neighbor_index != parent_index:
                cycle = self._dfs_cycle_detection(neighbor_index, current_index, visited)
                if cycle:
                    if current_index in cycle:
                        return cycle
                    return [current_index] + cycle

        return None

# Test program
def main():
    # Define the adjacency matrix and corresponding vertices
    
    adjacency_matrix_with_cycles = [
        [0, 1, 0, 0, 1, 0, 0],  # A
        [1, 0, 1, 0, 0, 0, 0],  # B
        [0, 1, 0, 1, 0, 0, 0],  # C
        [0, 0, 1, 0, 1, 0, 0],  # D
        [1, 0, 0, 1, 0, 1, 0],  # E
        [0, 0, 0, 0, 1, 0, 1],  # F
        [0, 0, 0, 0, 0, 1, 0]   # G
    ]
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Create the graph
    graph1 = Graph(vertices, adjacency_matrix_with_cycles)

    # Perform BFS starting from vertex 'A' (index 0)
    bfs_result1, mst_edges1 = graph1.bfs_mst(0)

    # Print the BFS traversal order
    print("BFS Traversal Order for graph with cycles:", ' '.join(bfs_result1))
    # Print the MST edges
    print("Minimum Spanning Tree Edges for graph with cycles:", ' '.join(map(str, mst_edges1)))

    # Find and print a cycle in the graph
    cycle1 = graph1.getACycle()
    if cycle1:
        cycle_labels = [graph1.vertices[i].label for i in cycle1]
        print("Cycle found:", ' -> '.join(cycle_labels))
    else:
        print("No cycle found.")

if __name__ == "__main__":
    main()
