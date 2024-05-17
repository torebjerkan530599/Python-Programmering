INFINITY = 1e+308 # Infinity value

# Boolean list

# Find single source shortest paths 
def getShortestPath(self, sourceVertex):
    # cost[v] stores the cost of the path from v to the source
    cost = [INFINITY] * self.getSize() # Initial cost to infinity
    cost[sourceVertex] = 0 # Cost of source is 0

    # parent[v] stores the previous vertex of v in the path
    parent = [-1] * self.getSize()
    
    # T stores the vertices whose path found so far
    T = []
    # isInT[v] is True if vertex v is in T
    isInT = [False] * self.getSize()
    
    # Expand T
    while len(T) < self.getSize():
        # Find smallest cost v in V - T 
        u = -1 # Vertex to be determined
        currentMinCost = INFINITY
        for i in range(self.getSize()):
        #Instead of using i not in T, we use not isInT[i] to check if a vertex is not in 𝑇
            if not isInT[i] and cost[i] < currentMinCost: #Not in T means V-T
                currentMinCost = cost[i]
                u = i

        if u == -1:
            break
        else:
            T.append(u) # Add a new vertex to T
            isInT[u] = True # Mark u as being in T
      
        # Adjust cost[v] for v that is adjacent to u and v in V - T
        for e in self.neighbors[u]:
            if not isInT[e.v] and cost[e.v] > cost[u] + e.weight: # kost[parent] + vekt til e
                cost[e.v] = cost[u] + e.weight
                parent[e.v] = u 

    return ShortestPathTree(sourceVertex, parent, T, cost, self.vertices)
