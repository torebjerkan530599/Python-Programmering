from WeightedGraph import WeightedGraph 

# Create vertices
vertices = ["Seattle", "San Francisco", "Los Angeles",
      "Denver", "Kansas City", "Chicago", "Boston", "New York",
      "Atlanta", "Miami", "Dallas", "Houston"];

# Create edges
edges = [
      [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
      [1, 0, 807], [1, 2, 381], [1, 3, 1267],
      [2, 1, 381], [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
      [3, 0, 1331], [3, 1, 1267], [3, 2, 1015], [3, 4, 599], 
        [3, 5, 1003],
      [4, 2, 1663], [4, 3, 599], [4, 5, 533], [4, 7, 1260],
        [4, 8, 864], [4, 10, 496],
      [5, 0, 2097], [5, 3, 1003], [5, 4, 533], 
        [5, 6, 983], [5, 7, 787],
      [6, 5, 983], [6, 7, 214],
      [7, 4, 1260], [7, 5, 787], [7, 6, 214], [7, 8, 888],
      [8, 4, 864], [8, 7, 888], [8, 9, 661], 
        [8, 10, 781], [8, 11, 810],
      [9, 8, 661], [9, 11, 1187],
      [10, 2, 1435], [10, 4, 496], [10, 8, 781], [10, 11, 239],
      [11, 8, 810], [11, 9, 1187], [11, 10, 239]
    ]

# Create a graph
graph1 = WeightedGraph(vertices, edges) 
print("The number of vertices in graph1: " + str(graph1.getSize()))
print("The vertex with index 1 is " + graph1.getVertex(1))
print("The index for Miami is " + str(graph1.getIndex("Miami")))
print("The edges for graph1: ")
graph1.printWeightedEdges()

#23.10
# previous_u = 0
# with open('graph.txt','w') as file:
#   file.write(f'{graph1.getSize()}\n')
#   for i,row in enumerate(edges):
#       if previous_u != row[0]:
#         file.write('\n')
#       u, v, w = row[0:3]
#       previous_u = u
#       if u < v:
#         string = f'{u},{v},{w}'
#         if i%3 < len(row) - 1:  # To prevent adding '|' at the end of the last line
#           string += ' |'
#         file.write(string + ' ')

with open('graph.txt', 'w') as file:
    file.write(f'{graph1.getSize()}\n')
    for i, row in enumerate(edges):
        u, v, w = row[0:3]
        if(u < v):
          file.write(f'{u}, {v}, {w}')
          if row[0] != edges[i + 1][0]:
              file.write('\n')
          else:
              file.write(' | ')

      
      
         
    #edges[u] = list(map(int, parts[3:])) # essentially an adjacency list
    #   #if i == 0 or i == 1:
    #   file.write(str(column)+',')
    #   #else:
    #   #  file.write(str(column)+'\n')
    # file.write('\n')    


# Create vertices and edges
# vertices = [x for x in range(5)]
# edges = [
#       [0, 1, 2], [0, 3, 8], 
#       [1, 0, 2], [1, 2, 7], [1, 3, 3],
#       [2, 1, 7], [2, 3, 4], [2, 4, 5],
#       [3, 0, 8], [3, 1, 3], [3, 2, 4], [3, 4, 6],
#       [4, 2, 5], [4, 3, 6]
#     ]
# graph2 = WeightedGraph(vertices, edges) # Create a graph
# print("\nThe edges for graph2:")
# graph2.printWeightedEdges()

  