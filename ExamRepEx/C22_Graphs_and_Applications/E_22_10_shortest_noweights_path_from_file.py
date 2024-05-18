from pathlib import Path
from queue import Queue

# Define the Graph class
class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges 
    def getAdjacencyLists(self, edges):
        neighbors = [[] for _ in range(len(self.vertices))]

        for i, edge_list in enumerate(edges):
            for v in edge_list:
                neighbors[i].append(v)

        return neighbors
    
    # Return the number of vertices in the graph 
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph 
    def getVertices(self):
        return self.vertices

    # Return the neighbors of vertex with the specified index 
    def getNeighbors(self, index):
        return self.neighbors[index]

# Function to find the shortest path between two vertices
def shortest_path(graph, start, end):
    if start not in graph.vertices or end not in graph.vertices:
        return "Invalid vertices"

    queue = Queue()
    visited = set()
    parent = {}

    queue.put(start)
    visited.add(start)
    parent[start] = None

    while not queue.empty():
        current = queue.get()

        if current == end:
            # Reconstruct the path
            path = [end]
            while parent[end] is not None:
                end = parent[end]
                path.append(end)
            return " -> ".join(map(str, reversed(path)))

        for neighbor in graph.getNeighbors(current):
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return "No path found"
# Main function to prompt user input and find the shortest path
def main():
    #filename = input("Enter the name of the file containing the graph: ")
    filename = Path(__file__).parent / 'connected_graph.txt'
    with open(filename, 'r') as file:
        num_vertices = int(file.readline().strip())
        edges = [list(map(int, line.split()))[1:] for line in file]

    graph = Graph(list(range(num_vertices)), edges)
    
    
        # Print vertices and edges
    print("The number of vertices is", num_vertices)
    for u in range(num_vertices):
        print(u, "(" + str(u) + "):", end=" ")
        for v in graph.getNeighbors(u):
            print("(" + str(u) + ", " + str(v) + ")", end=" ")
        print()

    start = int(input("Enter the starting vertex: "))
    end = int(input("Enter the ending vertex: "))

    shortest = shortest_path(graph, start, end)
    print("Shortest path:", shortest)

if __name__ == "__main__":
    main()