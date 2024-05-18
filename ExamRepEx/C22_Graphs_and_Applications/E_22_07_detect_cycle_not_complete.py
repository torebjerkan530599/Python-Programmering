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

    def getACycle(self):
        parent = [-1] * len(self.vertices)
        for start_index in range(len(self.vertices)):
            if not self.vertices[start_index].visited:
                cycle = self._bfs_cycle_detection(start_index, parent)
                if cycle:
                    self.reset_visits()
                    return cycle
        self.reset_visits()
        return None

    def _bfs_cycle_detection(self, start_index, parent):
        queue = Queue()
        self.vertices[start_index].visited = True
        queue.put(start_index)

        while not queue.empty():
            current_index = queue.get()

            for neighbor_index in self.neighbors[current_index]:
                if not self.vertices[neighbor_index].visited:
                    self.vertices[neighbor_index].visited = True
                    parent[neighbor_index] = current_index
                    queue.put(neighbor_index)
                elif parent[current_index] != neighbor_index:
                    # Cycle detected
                    return self._reconstruct_cycle(parent, current_index, neighbor_index)
        return None

    def _reconstruct_cycle(self, parent, start, end):
        cycle = []
        cycle.append(self.vertices[end].label)
        current = start
        while current != end:
            cycle.append(self.vertices[current].label)
            current = parent[current]
        cycle.append(self.vertices[end].label)
        return cycle[::-1]

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
    
    adjacency_matrix_with_cycles  =[
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
    graph1 = Graph(vertices, adjacency_matrix)
    graph2 = Graph(vertices, adjacency_matrix_with_cycles)
    
    # Perform BFS starting from vertex 'A' (index 0)
    bfs_result1, mst_edges1 = graph1.bfs_mst(0)
    bfs_result2, mst_edges2 = graph2.bfs_mst(0)

    # Print the BFS traversal order
    print("BFS Traversal Order:", ' '.join(bfs_result1))
    print("BFS Traversal Order:", ' '.join(bfs_result2))
    # Print the MST edges
    print("Minimum Spanning Tree Edges for graph without cycles:", ' '.join(map(str, mst_edges1)))
    print("Minimum Spanning Tree Edges for graph with cycles:", ' '.join(map(str, mst_edges2)))
    # Find and print a cycle in the graph
    cycle1, cycle2 = graph1.getACycle(), graph2.getACycle()
    
    result1 = "Cycle found:", ' -> '.join(cycle1) if cycle1 else "No cycle found."
    result2 = "Cycle found:", ' -> '.join(cycle2) if cycle2 else "No cycle found."
    
    print(f'result from graph without cycles: {result1}')    
    print(f'result from graph with cycles: {result2}')
    
if __name__ == "__main__":
    main()
