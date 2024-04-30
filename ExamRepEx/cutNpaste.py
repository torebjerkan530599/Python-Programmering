# Compute the distance between two points (x1, y1) and (x2, y2)
# Brute force solution O(n2)
def distance(x1, y1, x2, y2):
    familiar_formula = ((x2 - x1) **2 + (y2 - y1) ** 2)**0.5
    curriculum_formula = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
def nearest_points(points):
# p1 and p2 are the indices in the points list
    p1, p2 = 0, 1 # Initial two points
    shortestDistance = distance(points[p1][0], points[p1][1],
    points[p2][0], points[p2][1]) # Initialize shortestDistance
    # Compute distance for every two points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
            points[j][0], points[j][1]) # Find distance
            
            if shortestDistance > d:
                p1, p2 = i, j # Update p1, p2
                shortestDistance = d # New shortestDistance
    return p1, p2, shortestDistance # Return p1, p2 and distance
    
def main():
    points = [[5.2,2.4],[1.7,1.2],[4.1,2.6],[6.5,4.9], [4.3,3.5],[5.4,6.7],[2.6,4.1],[3.0,6.3],[1.7,3.2]]
    p1, p2, dist = nearest_points(points)
    print(f"The nearest points are \
    {points[p1]} and {points[p2]}, with distance {dist:0.3f}")

if __name__ == "__main__":
    main()