def maxInducedSubgraph(graph, k):
    # Function to get the degree of a vertex in the graph
    def degree(vertex):
        return len(graph[vertex])
    
    # Initialize a list to store vertices with degree less than k
    vertices_to_remove = [vertex for vertex in graph if degree(vertex) < k]
    
    # Initialize the induced subgraph as a copy of the original graph
    induced_subgraph = graph.copy()
    
    # Keep iterating until no vertices can be removed
    while vertices_to_remove:
        # Get the vertex to remove
        vertex = vertices_to_remove.pop()
        
        # Check if the vertex still exists in the induced subgraph
        if vertex in induced_subgraph:
            # Remove the vertex and its incident edges from the induced subgraph
            for neighbor in induced_subgraph[vertex]:
                induced_subgraph[neighbor].remove(vertex)
            del induced_subgraph[vertex]
            
            # Update the list of vertices to remove based on the updated induced subgraph
            vertices_to_remove = [v for v in induced_subgraph if degree(v) < k]
    
    # Check if any vertex remains in the induced subgraph
    if induced_subgraph:
        return induced_subgraph
    else:
        return None

# Example usage:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}
k = 2
print(maxInducedSubgraph(graph, k))
