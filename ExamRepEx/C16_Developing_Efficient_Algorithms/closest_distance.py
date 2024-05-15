import math

#alternative approach, only printing distance

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return min(euclidean_distance(points[i], points[j]) for i in range(n) for j in range(i+1, n))
    
    points.sort(key=lambda x: x[0])
    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    min_dist_left = closest_pair(left_half)
    min_dist_right = closest_pair(right_half)
    
    min_dist = min(min_dist_left, min_dist_right)
    
    strip = [point for point in points if abs(point[0] - points[mid][0]) < min_dist]
    strip.sort(key=lambda x: x[1])
    
    min_strip = float('inf')
    for i in range(len(strip)):
        for j in range(i+1, min(i+8, len(strip))):
            min_strip = min(min_strip, euclidean_distance(strip[i], strip[j]))
    
    return min(min_dist, min_strip)


# Example usage:
points = [(5.2, 2.4), (1.7, 1.2), (4.1, 2.6), (6.5, 4.9), (4.3, 3.5), (5.4, 6.7), (2.6, 4.1), (3.0, 6.3), (1.7, 3.2)]
print("Closest distance:", closest_pair(points))