import heapq
#from MinHeap import MinHeap
from pathlib import Path

class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]
    
    def add_edge(self, u, v, weight):
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
            edges = line.strip().split(' | ')
            for edge in edges:
                u, v, weight = map(int, edge.split(','))
                graph.add_edge(u, v, weight)
    return graph

def main():
    # file_url = input("Enter the URL of the file: ")
    source = int(input("Enter the source vertex: "))
    destination = int(input("Enter the destination vertex: "))

    # Download the file from the URL
    #import urllib.request
    #local_file, headers = urllib.request.urlretrieve(file_url)
    local_file = Path(__file__).parent / 'weighted_graph.txt'
    graph = read_graph_from_file(local_file)
    shortest_path = graph.get_shortest_path(source, destination)

    print("The shortest path between {} and {} is: {}".format(source, destination, ' '.join(map(str, shortest_path))))

if __name__ == "__main__":
    main()
