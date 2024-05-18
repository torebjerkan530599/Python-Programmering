from UnionFind import UnionFind

class KruskalMST:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
    
    def find_mst(self):
        # Sort edges by weight
        self.edges.sort(key=lambda edge: edge[2])
        
        # Initialize union-find structure
        uf = UnionFind(len(self.vertices))
        
        mst_edges = []
        total_weight = 0
        
        for u, v, weight in self.edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst_edges.append((u, v, weight))
                total_weight += weight
                # If we have enough edges for the MST, we can stop
                if len(mst_edges) == len(self.vertices) - 1:
                    break
        
        return mst_edges, total_weight

# Example usage
def main():
    # Example graph from the problem statement
    vertices = ['Amsterdam', 'Athens', 'Berlin', 'Brussels', 'Paris', 'Madrid', 'Lisbon']
    edges = [
        ('Amsterdam', 'Athens', 2873),
        ('Amsterdam', 'Berlin', 667),
        ('Amsterdam', 'Brussels', 212),
        ('Athens', 'Berlin', 2045),
        ('Athens', 'Brussels', 3027),
        ('Berlin', 'Brussels', 651),
        ('Berlin', 'Paris', 1050),
        ('Brussels', 'Paris', 316),
        ('Paris', 'Madrid', 1053),
        ('Madrid', 'Lisbon', 624),
        ('Paris', 'Lisbon', 1731),
        ('Amsterdam', 'Paris', 500)
    ]
    
    vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}
    indexed_edges = [(vertex_indices[u], vertex_indices[v], weight) for u, v, weight in edges]
    
    kruskal = KruskalMST(vertices, indexed_edges)
    mst_edges, total_weight = kruskal.find_mst()
    
    print("Edges in the MST:")
    for u, v, weight in mst_edges:
        print(f"{vertices[u]} - {vertices[v]}: {weight}")
    
    print(f"Total weight of the MST: {total_weight}")

if __name__ == "__main__":
    main()
