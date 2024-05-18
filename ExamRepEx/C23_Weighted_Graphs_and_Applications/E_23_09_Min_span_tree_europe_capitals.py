from pathlib import Path
from WeightedGraph import WeightedGraph

def read_graph_from_file(file_path):
    vertices = []
    edges = []
    vertex_to_index = {}    
    with open(file_path, 'r') as file:
        for line in file:
            capital1, capital2, weight = line.strip().split(',')
            weight = int(weight)    
            # Add vertices to the list and map if not already added
            if capital1 not in vertex_to_index:
                vertex_to_index[capital1] = len(vertices)
                vertices.append(capital1)
            if capital2 not in vertex_to_index:
                vertex_to_index[capital2] = len(vertices)
                vertices.append(capital2)   
            u = vertex_to_index[capital1]
            v = vertex_to_index[capital2]   
            edges.append((u, v, weight))
            edges.append((v, u, weight))    
    return vertices, edges


def print_weighted_edges(edges):
    print("Weighted edges in the graph:")
    for edge in edges:
        print(f"{edge[0]} - {edge[1]} ({edge[2]})")
        
def print_minimum_spanning_tree(mst_edges, total_weight):
    print(f"\nThe weight of the minimum spanning tree is: {total_weight}")
    print("Minimum Spanning Tree:")
    for edge in mst_edges:
        print(f"{edge[0]} - {edge[1]} ({edge[2]})")

def main():
    file_path = Path(__file__).parent /'Capitals.txt'
    
    # Read vertices and edges from file
    vertices, edges = read_graph_from_file(file_path)
    
    # Create an instance of WeightedGraph
    g = WeightedGraph(vertices, edges)
    
    # Print all weighted edges
    g.printWeightedEdges()
    
    # Find and display the minimum spanning tree
    tree = g.getMinimumSpanningTree()
    print("The weight of the minimum spanning tree is:", tree.getTotalWeight())
    tree.printTree()

if __name__ == "__main__":
    main()

# Example test case
# def main():
# Alternative test data:
#   A,B,5
#   A,C,3
#   B,C,4
#   B,D,2
#   C,D,7
#     vertices = ['Amsterdam', 'Athens', 'Berlin', 'Brussels', 'Paris', 'Madrid', 'Lisbon']
#     edges = [
#         ('Amsterdam', 'Athens', 2873),
#         ('Amsterdam', 'Berlin', 667),
#         ('Amsterdam', 'Brussels', 212),
#         ('Athens', 'Berlin', 2045),
#         ('Athens', 'Brussels', 3027),
#         ('Berlin', 'Brussels', 651),
#         ('Berlin', 'Paris', 1050),
#         ('Brussels', 'Paris', 316),
#         ('Paris', 'Madrid', 1053),
#         ('Madrid', 'Lisbon', 624),
#         ('Paris', 'Lisbon', 1731),
#         ('Amsterdam', 'Paris', 500)
#     ]
    
#     vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}
#     indexed_edges = [(vertex_indices[u], vertex_indices[v], weight) for u, v, weight in edges]
    
#     g = WeightedGraph(vertices, indexed_edges)
#     g.printWeightedEdges()
    
#     mst = g.getMinimumSpanningTree()
#     print("The weight of the minimum spanning tree is:", mst.getTotalWeight())
#     mst.printTree()

# if __name__ == "__main__":
#     main()
