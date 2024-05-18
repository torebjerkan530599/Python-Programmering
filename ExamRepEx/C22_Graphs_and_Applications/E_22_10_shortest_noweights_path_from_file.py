from pathlib import Path
from queue import Queue
import heapq
import sys

class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    def getAdjacencyLists(self, edges):
        neighbors = [[] for _ in range(len(self.vertices))]
        for u, *v in edges:  # Using *v to capture all remaining values after u
            u = int(u)
            for vertex in v:
                v = int(vertex)
                neighbors[u].append(Edge(u, v))
                neighbors[v].append(Edge(v, u))  # For undirected graph
        return neighbors

    # Other methods remain the same

    def dijkstra_shortest_path(self, start, end):
        # Initialize distances and visited array
        distances = [float('inf')] * len(self.vertices)
        distances[start] = 0
        visited = [False] * len(self.vertices)

        # Initialize a priority queue for Dijkstra's algorithm
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            dist_u, u = heapq.heappop(pq)
            visited[u] = True

            if u == end:
                break

            for edge in self.neighbors[u]:
                v = edge.v
                if not visited[v]:
                    new_dist = distances[u] + 1  # Since the graph is unweighted
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))

        # Reconstruct the path
        path = []
        if distances[end] != float('inf'):
            current = end
            while current != start:
                path.append(current)
                for edge in self.neighbors[current]:
                    if distances[edge.u] == distances[current] - 1:
                        current = edge.u
                        break
            path.append(start)
            path.reverse()

        return path
    
# The Edge class for defining an edge from u to v        
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

# Example usage:
if __name__ == "__main__":
    # Read the graph from file
    #filename = input("Enter the name of the file: ")
    filename = Path(__file__).parent / 'connected_graph.txt'
    with open(filename, 'r') as file:
        num_vertices = int(file.readline())
        edges = [list(map(int, line.split())) for line in file]

    # Create the graph
    vertices = list(range(num_vertices))
    graph = Graph(vertices, edges)

    # Prompt user for two vertices
    start_vertex = int(input("Enter the start vertex: "))
    end_vertex = int(input("Enter the end vertex: "))

    # Find shortest path
    shortest_path = graph.dijkstra_shortest_path(start_vertex, end_vertex)
    if shortest_path:
        print("Shortest path from", start_vertex, "to", end_vertex, ":", shortest_path)
    else:
        print("There is no path from", start_vertex, "to", end_vertex)

'''
import heapq
from pathlib import Path

class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]
    
    def add_edge(self, u, v, weight=1):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def get_shortest_path(self, source, destination):
        INFINITY = float('inf')
        cost = [INFINITY] * self.size
        cost[source] = 0
        parent = [-1] * self.size
        min_heap = [(0, source)]

        while min_heap:
            current_cost, u = heapq.heappop(min_heap)
            if u == destination:
                break

            for v, weight in self.adjacency_list[u]:
                if cost[v] > current_cost + weight:
                    cost[v] = current_cost + weight
                    parent[v] = u
                    heapq.heappush(min_heap, (cost[v], v))
                    

        path = []
        current = destination
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path

def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        size = int(file.readline().strip())
        graph = Graph(size)
        for line in file:
            edges = line.strip().split(' ')
            u = int(edges[0])
            for v in map(int, edges[1:]):
                graph.add_edge(u, v)
    return graph

def main():
    file_path = input("Enter the path to the file containing the graph: ")
    source = int(input("Enter the source vertex: "))
    destination = int(input("Enter the destination vertex: "))

    graph = read_graph_from_file(file_path)
    shortest_path = graph.get_shortest_path(source, destination)

    print("The shortest path between {} and {} is: {}".format(source, destination, ' '.join(map(str, shortest_path))))

if __name__ == "__main__":
    main()

'''