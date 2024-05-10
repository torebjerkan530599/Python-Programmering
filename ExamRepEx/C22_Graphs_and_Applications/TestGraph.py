from Graph import Graph

# Create vertices for graph in Figure 22.1
vertices = ["Seattle", "San Francisco", "Los Angeles",
    "Denver", "Kansas City", "Chicago", "Boston", "New York",
    "Atlanta", "Miami", "Dallas", "Houston"]

# Create an edge list for graph in Figure 22.1
edges = [
    [0, 1], [0, 3], [0, 5],
    [1, 0], [1, 2], [1, 3],
    [2, 1], [2, 3], [2, 4], [2, 10],
    [3, 0], [3, 1], [3, 2], [3, 4], [3, 5],
    [4, 2], [4, 3], [4, 5], [4, 7], [4, 8], [4, 10],
    [5, 0], [5, 3], [5, 4], [5, 6], [5, 7],
    [6, 5], [6, 7],
    [7, 4], [7, 5], [7, 6], [7, 8],
    [8, 4], [8, 7], [8, 9], [8, 10], [8, 11],
    [9, 8], [9, 11],
    [10, 2], [10, 4], [10, 8], [10, 11],
    [11, 8], [11, 9], [11, 10]
  ]

graph1 = Graph(vertices,edges) # Create graph1
neighbors = graph1.getAdjacnecyLists(edges)

'''#build edgelist, functions from Graph
    def getAdjacnecyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(u, v)) # Insert an edge (u, v)

        return neighbors
'''

# making sense of the matrix
for u in range(0, len(neighbors)):
    print(str(graph1.getVertex(u)), end = ": ")
    for j in range(len(graph1.getNeighbors(u))):
        print(f'({u},{neighbors[u][j].v})', end = ' ')
    print()

graph1.getIndex(0)
  # Print the edges, functions from Graph
    # def printEdges(self):
    #     for u in range(0, len(self.neighbors)):
    #         print(str(self.getVertex(u)) + " (" + str(u), end = "): ")
    #         for j in range(len(self.neighbors[u])):
    #             print("(" + str(u) + ", " + 
    #                   str(self.neighbors[u][j].v), end = ") ")
    #         print()

'''

'''
  

# print("The vertices in graph1: " + str(graph1.getVertices()))
# print("The number of vertices in graph1: " + str(graph1.getSize()))
# print("The vertex with index 1 is " + graph1.getVertex(1))
# print("The index for Miami is " + str(graph1.getIndex("Miami")))
# print("The degree for Miami is " + str(graph1.getDegree("Miami")))
# print("The edges for graph1:")
# graph1.printEdges()
    
# graph1.addVertex("Savannah")
# graph1.addEdge("Atlanta", "Savannah")
# graph1.addEdge("Savannah", "Atlanta")
# print("\nThe edges for graph1 after adding a new vertex and edges:")
# graph1.printEdges()

# # List of Edge objects for graph in Figure 22.3a
# names = ["Peter", "Jane", "Mark", "Cindy", "Wendy"]
# edges = [[0, 2], [1, 2], [2, 4], [3, 4]]

# # Create a graph with 5 vertices
# graph2 = Graph(names, edges)
# print("\nThe number of vertices in graph2: " 
#       + str(graph2.getSize()))
# print("The edges for graph2:")
# graph2.printEdges()
